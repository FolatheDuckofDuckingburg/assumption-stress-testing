"""SQLite persistence for AST-RI bibliographic source records."""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3
from typing import Iterator

from .models import Source, SourceType


class DuplicateSourceError(ValueError):
    """Raised when a DOI, arXiv ID, URL, or source ID already exists."""


class SourceNotFoundError(LookupError):
    """Raised when a requested source identifier is not in the registry."""


class SourceRegistry:
    """A small local registry with no network or full-text ingestion."""

    def __init__(self, database_path: str | Path = "ast_ri_sources.sqlite3") -> None:
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS sources (
                    source_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    authors_json TEXT NOT NULL,
                    source_type TEXT NOT NULL,
                    year INTEGER,
                    published_date TEXT,
                    doi TEXT UNIQUE,
                    arxiv_id TEXT UNIQUE,
                    url TEXT UNIQUE,
                    created_at TEXT NOT NULL DEFAULT (
                        strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                    )
                )
                """
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_sources_title ON sources(title)"
            )

    @staticmethod
    def _to_source(row: sqlite3.Row) -> Source:
        return Source(
            source_id=row["source_id"],
            title=row["title"],
            authors=tuple(json.loads(row["authors_json"])),
            source_type=SourceType(row["source_type"]),
            year=row["year"],
            published_date=row["published_date"],
            doi=row["doi"],
            arxiv_id=row["arxiv_id"],
            url=row["url"],
        )

    def add_source(self, source: Source) -> Source:
        """Insert a source, rejecting duplicate identifiers rather than merging."""
        try:
            with self._connect() as connection:
                connection.execute(
                    """
                    INSERT INTO sources (
                        source_id, title, authors_json, source_type, year,
                        published_date, doi, arxiv_id, url
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        source.source_id,
                        source.title,
                        json.dumps(source.authors, ensure_ascii=False),
                        source.source_type.value,
                        source.year,
                        source.published_date,
                        source.doi,
                        source.arxiv_id,
                        source.url,
                    ),
                )
        except sqlite3.IntegrityError as exc:
            raise DuplicateSourceError(
                "A source with this source ID, DOI, arXiv ID, or URL already exists."
            ) from exc
        return source

    def get_source(self, source_id: str) -> Source:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM sources WHERE source_id = ?", (source_id,)
            ).fetchone()
        if row is None:
            raise SourceNotFoundError(source_id)
        return self._to_source(row)

    def find_by_doi(self, doi: str) -> Source | None:
        from .models import normalize_doi

        normalized = normalize_doi(doi)
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM sources WHERE doi = ?", (normalized,)
            ).fetchone()
        return self._to_source(row) if row else None

    def find_by_arxiv_id(self, arxiv_id: str) -> Source | None:
        from .models import normalize_arxiv_id

        normalized = normalize_arxiv_id(arxiv_id)
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM sources WHERE arxiv_id = ?", (normalized,)
            ).fetchone()
        return self._to_source(row) if row else None

    def search(self, query: str, limit: int = 50) -> list[Source]:
        """Case-insensitive title/author search; user input is SQL-parameterized."""
        if limit < 1:
            raise ValueError("limit must be at least 1.")
        term = f"%{query.strip()}%"
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT * FROM sources
                WHERE title LIKE ? COLLATE NOCASE
                   OR authors_json LIKE ? COLLATE NOCASE
                ORDER BY year DESC, title COLLATE NOCASE
                LIMIT ?
                """,
                (term, term, limit),
            ).fetchall()
        return [self._to_source(row) for row in rows]

    def list_sources(self, limit: int = 100, offset: int = 0) -> list[Source]:
        if limit < 1 or offset < 0:
            raise ValueError("limit must be positive and offset must be non-negative.")
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT * FROM sources
                ORDER BY year DESC, title COLLATE NOCASE
                LIMIT ? OFFSET ?
                """,
                (limit, offset),
            ).fetchall()
        return [self._to_source(row) for row in rows]

    def count(self) -> int:
        with self._connect() as connection:
            row = connection.execute("SELECT COUNT(*) AS n FROM sources").fetchone()
        return int(row["n"])
