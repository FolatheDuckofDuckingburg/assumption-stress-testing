"""Auditable human relevance reviews for AST-RI literature candidates."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
import sqlite3

from .models import Source
from .registry import SourceNotFoundError, SourceRegistry


class RelevanceStatus(str, Enum):
    IN_SCOPE = "in_scope"
    UNCERTAIN = "uncertain"
    OUT_OF_SCOPE = "out_of_scope"


@dataclass(frozen=True, slots=True)
class RelevanceReview:
    source_id: str
    status: RelevanceStatus
    rationale: str
    assessor: str
    reviewed_at: str


@dataclass(frozen=True, slots=True)
class RelevanceQueueItem:
    source: Source
    status: RelevanceStatus
    rationale: str | None
    assessor: str | None
    reviewed_at: str | None


class RelevanceReviewStore:
    """Append-only human review history; new sources default to UNCERTAIN."""

    def __init__(self, database_path: str | Path | SourceRegistry) -> None:
        if isinstance(database_path, SourceRegistry):
            self.database_path = database_path.database_path
        else:
            self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.database_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS relevance_reviews (
                    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_id TEXT NOT NULL REFERENCES sources(source_id),
                    status TEXT NOT NULL CHECK (
                        status IN ('in_scope', 'uncertain', 'out_of_scope')
                    ),
                    rationale TEXT NOT NULL,
                    assessor TEXT NOT NULL,
                    reviewed_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_relevance_source_review "
                "ON relevance_reviews(source_id, review_id DESC)"
            )

    def record_review(
        self,
        source_id: str,
        status: RelevanceStatus,
        rationale: str,
        assessor: str,
    ) -> RelevanceReview:
        try:
            normalized_status = RelevanceStatus(status)
        except ValueError as exc:
            raise ValueError(f"Unsupported relevance status: {status!r}") from exc
        rationale = rationale.strip()
        assessor = assessor.strip()
        if not rationale:
            raise ValueError("A review rationale is required.")
        if not assessor:
            raise ValueError("An assessor identifier is required.")
        with sqlite3.connect(self.database_path) as connection:
            exists = connection.execute(
                "SELECT 1 FROM sources WHERE source_id = ?", (source_id,)
            ).fetchone()
            if exists is None:
                raise SourceNotFoundError(source_id)
            reviewed_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            connection.execute(
                """
                INSERT INTO relevance_reviews
                    (source_id, status, rationale, assessor, reviewed_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (source_id, normalized_status.value, rationale, assessor, reviewed_at),
            )
        return RelevanceReview(
            source_id, normalized_status, rationale, assessor, reviewed_at
        )

    def current_review(self, source_id: str) -> RelevanceReview | None:
        with sqlite3.connect(self.database_path) as connection:
            row = connection.execute(
                """
                SELECT source_id, status, rationale, assessor, reviewed_at
                FROM relevance_reviews WHERE source_id = ?
                ORDER BY review_id DESC LIMIT 1
                """,
                (source_id,),
            ).fetchone()
        if row is None:
            return None
        return RelevanceReview(
            row[0], RelevanceStatus(row[1]), row[2], row[3], row[4]
        )

    def list_queue(
        self,
        registry: SourceRegistry,
        *,
        status: RelevanceStatus | None = RelevanceStatus.UNCERTAIN,
        limit: int = 100,
        offset: int = 0,
    ) -> list[RelevanceQueueItem]:
        if limit < 1 or offset < 0:
            raise ValueError("limit must be positive and offset non-negative.")
        status_value = RelevanceStatus(status).value if status is not None else None
        sql = """
            WITH latest AS (
                SELECT r.* FROM relevance_reviews r
                JOIN (
                    SELECT source_id, MAX(review_id) AS latest_id
                    FROM relevance_reviews GROUP BY source_id
                ) newest ON newest.latest_id = r.review_id
            )
            SELECT s.source_id, COALESCE(latest.status, 'uncertain') AS status,
                   latest.rationale, latest.assessor, latest.reviewed_at
            FROM sources s LEFT JOIN latest ON latest.source_id = s.source_id
        """
        params: list[object] = []
        if status_value is not None:
            sql += " WHERE COALESCE(latest.status, 'uncertain') = ?"
            params.append(status_value)
        sql += " ORDER BY s.year DESC, s.title COLLATE NOCASE LIMIT ? OFFSET ?"
        params.extend((limit, offset))
        with sqlite3.connect(self.database_path) as connection:
            rows = connection.execute(sql, params).fetchall()
        items: list[RelevanceQueueItem] = []
        for source_id, status_text, rationale, assessor, reviewed_at in rows:
            items.append(RelevanceQueueItem(
                source=registry.get_source(source_id),
                status=RelevanceStatus(status_text),
                rationale=rationale,
                assessor=assessor,
                reviewed_at=reviewed_at,
            ))
        return items
