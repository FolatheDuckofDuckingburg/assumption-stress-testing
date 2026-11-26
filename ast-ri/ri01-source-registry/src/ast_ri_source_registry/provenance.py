"""Persistence helpers for provider metadata provenance."""

from __future__ import annotations

from dataclasses import asdict
import json
import sqlite3

from .providers import ProviderRecord


def initialize_provenance_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS provider_records (
            provider_record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id TEXT NOT NULL,
            provider TEXT NOT NULL,
            provider_item_id TEXT NOT NULL,
            retrieved_at TEXT NOT NULL,
            metadata_json TEXT NOT NULL,
            UNIQUE(provider, provider_item_id, retrieved_at),
            FOREIGN KEY(source_id) REFERENCES sources(source_id)
        )
        """
    )
    connection.execute(
        "CREATE INDEX IF NOT EXISTS idx_provider_source ON provider_records(source_id)"
    )


def store_provider_record(connection: sqlite3.Connection, record: ProviderRecord) -> int:
    """Persist the provider snapshot associated with an already-stored source."""
    source = record.source
    metadata = {
        "title": source.title,
        "authors": list(source.authors),
        "source_type": source.source_type.value,
        "year": source.year,
        "published_date": source.published_date,
        "doi": source.doi,
        "arxiv_id": source.arxiv_id,
        "url": source.url,
    }
    cursor = connection.execute(
        """
        INSERT INTO provider_records (
            source_id, provider, provider_item_id, retrieved_at, metadata_json
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (
            source.source_id,
            record.provider,
            record.provider_record_id,
            record.retrieved_at,
            json.dumps(metadata, ensure_ascii=False, sort_keys=True),
        ),
    )
    return int(cursor.lastrowid)


def list_provider_records(connection: sqlite3.Connection, source_id: str) -> list[dict]:
    rows = connection.execute(
        """
        SELECT provider, provider_item_id, retrieved_at, metadata_json
        FROM provider_records
        WHERE source_id = ?
        ORDER BY retrieved_at, provider
        """,
        (source_id,),
    ).fetchall()
    return [
        {
            "provider": row["provider"],
            "provider_item_id": row["provider_item_id"],
            "retrieved_at": row["retrieved_at"],
            "metadata": json.loads(row["metadata_json"]),
        }
        for row in rows
    ]
