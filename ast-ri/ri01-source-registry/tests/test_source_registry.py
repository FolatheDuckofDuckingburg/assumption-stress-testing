from pathlib import Path
import tempfile
import unittest

from ast_ri_source_registry import (
    DuplicateSourceError,
    Source,
    SourceRegistry,
    SourceType,
    SourceValidationError,
)


class SourceModelTests(unittest.TestCase):
    def test_normalizes_doi_and_arxiv_identifier(self):
        source = Source(
            title="A theoretical physics paper",
            authors=(" A. Researcher ", "B. Scientist"),
            doi="https://doi.org/10.1000/ABC.123",
            arxiv_id="https://arxiv.org/abs/2301.01234v2",
            source_type=SourceType.PREPRINT,
        )
        self.assertEqual(source.doi, "10.1000/abc.123")
        self.assertEqual(source.arxiv_id, "2301.01234v2")
        self.assertEqual(source.authors, ("A. Researcher", "B. Scientist"))
        self.assertTrue(source.source_id.startswith("src_"))

    def test_rejects_missing_identifiers(self):
        with self.assertRaises(SourceValidationError):
            Source(title="No identifier", authors=("A. Researcher",))

    def test_rejects_invalid_doi(self):
        with self.assertRaises(SourceValidationError):
            Source(
                title="Bad DOI",
                authors=("A. Researcher",),
                doi="not-a-doi",
            )


class SourceRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        database = Path(self.temp_dir.name) / "sources.sqlite3"
        self.registry = SourceRegistry(database)

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_source(self, **overrides):
        values = {
            "title": "On the Schwarzschild solution",
            "authors": ("A. Researcher",),
            "year": 1916,
            "doi": "10.1000/schwarzschild",
            "url": "https://example.org/schwarzschild",
            "source_type": SourceType.JOURNAL_ARTICLE,
        }
        values.update(overrides)
        return Source(**values)

    def test_add_and_retrieve_source(self):
        source = self.make_source()
        self.registry.add_source(source)
        retrieved = self.registry.get_source(source.source_id)
        self.assertEqual(retrieved, source)
        self.assertEqual(self.registry.count(), 1)

    def test_duplicate_doi_is_rejected(self):
        self.registry.add_source(self.make_source())
        duplicate = self.make_source(
            title="A differently titled duplicate",
            url="https://example.org/another-url",
        )
        with self.assertRaises(DuplicateSourceError):
            self.registry.add_source(duplicate)

    def test_lookup_by_doi_is_normalized(self):
        source = self.make_source()
        self.registry.add_source(source)
        found = self.registry.find_by_doi("https://doi.org/10.1000/SCHWARZSCHILD")
        self.assertEqual(found, source)

    def test_search_matches_title_and_author(self):
        source = self.make_source()
        self.registry.add_source(source)
        self.assertEqual(self.registry.search("schwarzschild"), [source])
        self.assertEqual(self.registry.search("researcher"), [source])

    def test_rejects_invalid_pagination(self):
        with self.assertRaises(ValueError):
            self.registry.list_sources(limit=0)
        with self.assertRaises(ValueError):
            self.registry.list_sources(offset=-1)


if __name__ == "__main__":
    unittest.main()
