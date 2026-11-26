import sqlite3
import unittest

from ast_ri_source_registry.models import Source
from ast_ri_source_registry.providers import ProviderRecord
from ast_ri_source_registry.provenance import (
    initialize_provenance_schema,
    list_provider_records,
    store_provider_record,
)


class ProvenanceTests(unittest.TestCase):
    def test_persists_provider_snapshot(self):
        connection = sqlite3.connect(":memory:")
        connection.row_factory = sqlite3.Row
        connection.execute(
            """
            CREATE TABLE sources (
                source_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                authors_json TEXT NOT NULL,
                source_type TEXT NOT NULL,
                year INTEGER,
                published_date TEXT,
                doi TEXT,
                arxiv_id TEXT,
                url TEXT
            )
            """
        )
        source = Source(
            title="A paper on causal structure",
            authors=("A. Researcher",),
            doi="10.1000/causal",
        )
        connection.execute(
            "INSERT INTO sources VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                source.source_id, source.title, '["A. Researcher"]',
                source.source_type.value, source.year, source.published_date,
                source.doi, source.arxiv_id, source.url,
            ),
        )
        initialize_provenance_schema(connection)
        record = ProviderRecord(
            source=source,
            provider="crossref",
            provider_record_id="10.1000/causal",
            retrieved_at="2026-01-01T00:00:00+00:00",
        )
        record_id = store_provider_record(connection, record)
        stored = list_provider_records(connection, source.source_id)
        self.assertEqual(record_id, 1)
        self.assertEqual(stored[0]["provider"], "crossref")
        self.assertEqual(stored[0]["metadata"]["title"], source.title)
        connection.close()


if __name__ == "__main__":
    unittest.main()
