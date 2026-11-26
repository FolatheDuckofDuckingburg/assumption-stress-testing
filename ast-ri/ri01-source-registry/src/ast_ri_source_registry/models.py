"""Validated bibliographic records for the AST-RI source registry."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
import hashlib
import re
from typing import Iterable
from urllib.parse import urlparse


class SourceType(str, Enum):
    PREPRINT = "preprint"
    JOURNAL_ARTICLE = "journal_article"
    BOOK = "book"
    REVIEW = "review"
    THESIS = "thesis"
    CONFERENCE_PAPER = "conference_paper"
    OTHER = "other"


class SourceValidationError(ValueError):
    """Raised when bibliographic metadata fails validation."""


_DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
_ARXIV_NEW_RE = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$", re.IGNORECASE)
_ARXIV_OLD_RE = re.compile(
    r"^[a-z][a-z0-9.-]+/\d{7}(?:v\d+)?$", re.IGNORECASE
)


def normalize_doi(value: str | None) -> str | None:
    if value is None:
        return None
    doi = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):].strip()
            break
    if not _DOI_RE.fullmatch(doi):
        raise SourceValidationError(f"Invalid DOI: {value!r}")
    return doi.lower()


def normalize_arxiv_id(value: str | None) -> str | None:
    if value is None:
        return None
    arxiv_id = value.strip()
    for prefix in (
        "https://arxiv.org/abs/",
        "http://arxiv.org/abs/",
        "arXiv:",
    ):
        if arxiv_id.lower().startswith(prefix.lower()):
            arxiv_id = arxiv_id[len(prefix):].strip()
            break
    if not (
        _ARXIV_NEW_RE.fullmatch(arxiv_id)
        or _ARXIV_OLD_RE.fullmatch(arxiv_id)
    ):
        raise SourceValidationError(f"Invalid arXiv identifier: {value!r}")
    return arxiv_id.lower()


def _validate_url(value: str | None) -> str | None:
    if value is None:
        return None
    url = value.strip()
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SourceValidationError("URL must be an absolute HTTP(S) URL.")
    return url


@dataclass(frozen=True, slots=True)
class Source:
    """A bibliographic record; it deliberately does not contain paper text."""

    title: str
    authors: tuple[str, ...]
    source_type: SourceType = SourceType.OTHER
    year: int | None = None
    published_date: str | None = None
    doi: str | None = None
    arxiv_id: str | None = None
    url: str | None = None
    source_id: str = ""

    def __post_init__(self) -> None:
        title = self.title.strip()
        if not title:
            raise SourceValidationError("Title must not be empty.")
        object.__setattr__(self, "title", title)

        authors = tuple(author.strip() for author in self.authors if author.strip())
        if not authors:
            raise SourceValidationError("At least one non-empty author is required.")
        object.__setattr__(self, "authors", authors)

        try:
            source_type = SourceType(self.source_type)
        except ValueError as exc:
            raise SourceValidationError(
                f"Unsupported source type: {self.source_type!r}"
            ) from exc
        object.__setattr__(self, "source_type", source_type)

        if self.year is not None and not 1000 <= self.year <= 9999:
            raise SourceValidationError("Year must be a four-digit year.")

        if self.published_date is not None:
            try:
                date.fromisoformat(self.published_date)
            except ValueError as exc:
                raise SourceValidationError(
                    "published_date must use ISO format YYYY-MM-DD."
                ) from exc

        doi = normalize_doi(self.doi)
        arxiv_id = normalize_arxiv_id(self.arxiv_id)
        url = _validate_url(self.url)
        object.__setattr__(self, "doi", doi)
        object.__setattr__(self, "arxiv_id", arxiv_id)
        object.__setattr__(self, "url", url)

        if not any((doi, arxiv_id, url)):
            raise SourceValidationError(
                "A source needs at least one stable identifier: DOI, arXiv ID, or URL."
            )

        if not self.source_id:
            identity = doi or arxiv_id or url
            digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
            object.__setattr__(self, "source_id", f"src_{digest}")


def authors_from(values: Iterable[str]) -> tuple[str, ...]:
    """Convenience helper for converting an author iterable into a tuple."""
    return tuple(values)
