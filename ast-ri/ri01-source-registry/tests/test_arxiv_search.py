import unittest

from ast_ri_source_registry.arxiv_search import (
    ALLOWED_ARXIV_CATEGORIES,
    ArxivSearchProvider,
    ArxivSearchValidationError,
    build_arxiv_search_query,
)
from ast_ri_source_registry.providers import ProviderError


ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <opensearch:totalResults>2</opensearch:totalResults>
  <entry>
    <id>http://arxiv.org/abs/2301.01234v2</id>
    <published>2023-01-03T00:00:00Z</published>
    <title>  Quantum   Fields and Gravity </title>
    <author><name>A. Researcher</name></author>
    <arxiv:doi>10.1234/example</arxiv:doi>
  </entry>
</feed>"""


class ArxivSearchTests(unittest.TestCase):
    def test_query_is_category_bounded(self):
        query = build_arxiv_search_query("black hole thermodynamics", ["gr-qc", "hep-th"])
        self.assertIn("cat:gr-qc OR cat:hep-th", query)
        self.assertIn('all:"black hole thermodynamics"', query)

    def test_rejects_out_of_scope_category(self):
        with self.assertRaises(ArxivSearchValidationError):
            build_arxiv_search_query("gravity", ["astro-ph"])

    def test_rejects_empty_query_and_invalid_pagination(self):
        with self.assertRaises(ArxivSearchValidationError):
            build_arxiv_search_query("  ", ["gr-qc"])
        provider = ArxivSearchProvider(transport=lambda *_: ATOM.encode())
        with self.assertRaises(ArxivSearchValidationError):
            provider.search("gravity", start=-1)
        with self.assertRaises(ArxivSearchValidationError):
            provider.search("gravity", max_results=101)

    def test_pagination_parameters_and_provenance(self):
        requested = []
        def transport(url, headers, timeout):
            requested.append(url)
            return ATOM.encode("utf-8")
        page = ArxivSearchProvider(transport=transport).search(
            "causal set", ["gr-qc", "hep-th"], start=25, max_results=10
        )
        self.assertEqual(len(page.records), 1)
        self.assertIn("start=25", requested[0])
        self.assertIn("max_results=10", requested[0])
        self.assertEqual(page.provenance.start, 25)
        self.assertEqual(page.provenance.total_results, 2)
        self.assertEqual(page.provenance.returned_results, 1)
        source = page.records[0].source
        self.assertEqual(source.arxiv_id, "2301.01234v2")
        self.assertEqual(source.doi, "10.1234/example")
        self.assertEqual(source.year, 2023)

    def test_malformed_xml_raises_provider_error(self):
        provider = ArxivSearchProvider(transport=lambda *_: b"<not-xml")
        with self.assertRaises(ProviderError):
            provider.search("gravity")

    def test_allowlist_is_explicit(self):
        self.assertEqual(
            ALLOWED_ARXIV_CATEGORIES,
            frozenset({"hep-th", "gr-qc", "math-ph", "quant-ph"}),
        )


if __name__ == "__main__":
    unittest.main()
