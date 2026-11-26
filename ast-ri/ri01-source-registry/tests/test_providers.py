import json
import unittest

from ast_ri_source_registry.providers import (
    ArxivProvider,
    CrossrefProvider,
    ProviderError,
    ProviderRecord,
    compare_provider_records,
)


ARXIV_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>https://arxiv.org/abs/2301.01234v2</id>
    <published>2023-01-03T12:00:00Z</published>
    <title>  A test of spacetime geometry  </title>
    <author><name>A. Researcher</name></author>
    <author><name>B. Scientist</name></author>
    <arxiv:doi>10.1000/example</arxiv:doi>
    <summary>Abstract text is not retained.</summary>
  </entry>
</feed>
"""


CROSSREF_JSON = json.dumps({
    "message": {
        "title": ["A test of spacetime geometry"],
        "author": [
            {"given": "A.", "family": "Researcher"},
            {"given": "B.", "family": "Scientist"},
        ],
        "published-print": {"date-parts": [[2023, 1, 3]]},
        "DOI": "10.1000/example",
        "URL": "https://api.crossref.org/works/10.1000/example",
        "type": "journal-article",
    }
}).encode("utf-8")


class ProviderTests(unittest.TestCase):
    def test_arxiv_record_normalization_and_provenance(self):
        calls = []

        def transport(url, headers, timeout):
            calls.append((url, headers, timeout))
            return ARXIV_XML

        record = ArxivProvider(transport=transport).fetch_by_id("2301.01234v2")
        self.assertEqual(record.provider, "arxiv")
        self.assertEqual(record.provider_record_id, "2301.01234v2")
        self.assertEqual(record.source.title, "A test of spacetime geometry")
        self.assertEqual(record.source.authors, ("A. Researcher", "B. Scientist"))
        self.assertEqual(record.source.doi, "10.1000/example")
        self.assertEqual(len(calls), 1)
        self.assertIn("User-Agent", calls[0][1])

    def test_crossref_record_normalization_and_provenance(self):
        record = CrossrefProvider(
            transport=lambda url, headers, timeout: CROSSREF_JSON
        ).fetch_by_doi("https://doi.org/10.1000/EXAMPLE")
        self.assertEqual(record.provider, "crossref")
        self.assertEqual(record.provider_record_id, "10.1000/example")
        self.assertEqual(record.source.year, 2023)
        self.assertEqual(record.source.published_date, "2023-01-03")
        self.assertEqual(record.source.authors[0], "A. Researcher")

    def test_crossref_handles_missing_publication_date(self):
        payload = json.dumps({"message": {
            "title": ["A metadata record without a date"],
            "author": [{"given": "A.", "family": "Researcher"}],
            "published-print": None,
            "published-online": None,
            "created": {"date-parts": []},
            "DOI": "10.1000/no-date",
            "type": "posted-content",
        }}).encode("utf-8")
        record = CrossrefProvider(
            transport=lambda *args: payload
        ).fetch_by_doi("10.1000/no-date")
        self.assertIsNone(record.source.year)
        self.assertEqual(record.source.source_type.value, "preprint")

    def test_provider_rejects_malformed_payload(self):
        with self.assertRaises(ProviderError):
            ArxivProvider(transport=lambda *args: b"<not-closed").fetch_by_id(
                "2301.01234"
            )

    def test_provider_disagreement_is_reported_not_resolved(self):
        from ast_ri_source_registry.models import Source

        first = ProviderRecord(
            source=Source(
                title="Original title",
                authors=("A. Researcher",),
                doi="10.1000/example",
            ),
            provider="crossref",
            provider_record_id="10.1000/example",
            retrieved_at="2026-01-01T00:00:00+00:00",
        )
        second = ProviderRecord(
            source=Source(
                title="Different title",
                authors=("A. Researcher",),
                doi="10.1000/example",
            ),
            provider="local",
            provider_record_id="local-1",
            retrieved_at="2026-01-02T00:00:00+00:00",
        )
        conflicts = compare_provider_records([first, second])
        self.assertEqual(conflicts["title"], ("Original title", "Different title"))
        self.assertNotIn("authors", conflicts)


if __name__ == "__main__":
    unittest.main()
