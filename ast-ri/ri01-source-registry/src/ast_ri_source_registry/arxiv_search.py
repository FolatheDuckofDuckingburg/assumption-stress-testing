"""Metadata-only arXiv search restricted to AST-RI theoretical-physics categories.

Search terms are encoded as literal all-field phrases; callers cannot inject
arXiv query syntax or broaden the category allowlist.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
from typing import Sequence
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

from .models import Source, SourceType, normalize_arxiv_id
from .providers import MetadataProvider, ProviderError, ProviderRecord


ALLOWED_ARXIV_CATEGORIES = frozenset({"hep-th", "gr-qc", "math-ph", "quant-ph"})
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_NS = "http://arxiv.org/schemas/atom"


class ArxivSearchValidationError(ValueError):
    """Raised when a search request violates AST-RI's bounded query policy."""


@dataclass(frozen=True, slots=True)
class SearchProvenance:
    query: str
    categories: tuple[str, ...]
    start: int
    max_results: int
    retrieved_at: str
    total_results: int
    returned_results: int


@dataclass(frozen=True, slots=True)
class ArxivSearchPage:
    records: tuple[ProviderRecord, ...]
    provenance: SearchProvenance


def _literal_query(query: str) -> str:
    cleaned = " ".join(query.split())
    if not cleaned:
        raise ArxivSearchValidationError("Search query must not be empty.")
    if len(cleaned) > 200:
        raise ArxivSearchValidationError("Search query must be at most 200 characters.")
    # Quoting plus removal of arXiv control characters keeps user input a phrase,
    # rather than allowing it to append OR/cat:/id_list query operators.
    phrase = re.sub(r'[\\\"{}()]', " ", cleaned)
    phrase = " ".join(phrase.split())
    if not phrase:
        raise ArxivSearchValidationError("Search query contains no searchable text.")
    return f'all:"{phrase}"'


def build_arxiv_search_query(query: str, categories: Sequence[str]) -> str:
    """Build a category-bounded arXiv query from literal user search text."""
    if not categories:
        raise ArxivSearchValidationError("At least one allowed category is required.")
    normalized = tuple(dict.fromkeys(str(category).strip().lower() for category in categories))
    invalid = sorted(set(normalized) - ALLOWED_ARXIV_CATEGORIES)
    if invalid:
        raise ArxivSearchValidationError(
            "Unsupported category; allowed categories are: "
            + ", ".join(sorted(ALLOWED_ARXIV_CATEGORIES))
        )
    if any(not category for category in normalized):
        raise ArxivSearchValidationError("Categories must not be empty.")
    category_clause = " OR ".join(f"cat:{category}" for category in normalized)
    return f"({category_clause}) AND ({_literal_query(query)})"


def _text(entry: ET.Element, path: str) -> str:
    return " ".join(entry.findtext(path, default="", namespaces=ATOM_NS).split())


def _entry_to_record(entry: ET.Element) -> ProviderRecord:
    raw_id = _text(entry, "atom:id")
    match = re.search(r"/abs/([^/?#]+)", raw_id)
    if not match:
        raise ProviderError("arXiv search result has no recognizable abstract identifier.")
    arxiv_id = normalize_arxiv_id(match.group(1))
    title = _text(entry, "atom:title")
    authors = tuple(
        " ".join((node.text or "").split())
        for node in entry.findall("atom:author/atom:name", ATOM_NS)
        if (node.text or "").strip()
    )
    published = _text(entry, "atom:published")
    published_date = published[:10] if published else None
    doi = entry.findtext(f"{{{ARXIV_NS}}}doi")
    if not title or not authors:
        raise ProviderError(f"arXiv result {arxiv_id} is missing title or authors.")
    year = int(published_date[:4]) if published_date else None
    source = Source(
        title=title,
        authors=authors,
        source_type=SourceType.PREPRINT,
        year=year,
        published_date=published_date,
        doi=doi,
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
    )
    return ProviderRecord(
        source=source,
        provider="arxiv",
        provider_record_id=arxiv_id,
        retrieved_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )


class ArxivSearchProvider(MetadataProvider):
    """Paginated arXiv Atom search constrained to theoretical-physics categories."""

    provider_name = "arxiv"
    API_URL = "https://export.arxiv.org/api/query"

    def search(
        self,
        query: str,
        categories: Sequence[str] = ("hep-th", "gr-qc", "math-ph", "quant-ph"),
        *,
        start: int = 0,
        max_results: int = 25,
        sort_by: str = "relevance",
        sort_order: str = "descending",
    ) -> ArxivSearchPage:
        if start < 0:
            raise ArxivSearchValidationError("start must be non-negative.")
        if not 1 <= max_results <= 100:
            raise ArxivSearchValidationError("max_results must be between 1 and 100.")
        if sort_by not in {"relevance", "lastUpdatedDate", "submittedDate"}:
            raise ArxivSearchValidationError("Unsupported sort_by value.")
        if sort_order not in {"ascending", "descending"}:
            raise ArxivSearchValidationError("Unsupported sort_order value.")

        search_query = build_arxiv_search_query(query, categories)
        normalized_categories = tuple(
            dict.fromkeys(str(category).strip().lower() for category in categories)
        )
        params = urlencode({
            "search_query": search_query,
            "start": start,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        })
        payload = self._get(f"{self.API_URL}?{params}")
        try:
            root = ET.fromstring(payload)
        except ET.ParseError as exc:
            raise ProviderError("arXiv returned malformed Atom XML.") from exc

        total_text = root.findtext("opensearch:totalResults", namespaces={
            **ATOM_NS, "opensearch": "http://a9.com/-/spec/opensearch/1.1/"
        })
        try:
            total_results = int(total_text or "0")
        except ValueError as exc:
            raise ProviderError("arXiv returned an invalid total-results count.") from exc

        entries = root.findall("atom:entry", ATOM_NS)
        records = tuple(_entry_to_record(entry) for entry in entries)
        retrieved_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        provenance = SearchProvenance(
            query=" ".join(query.split()),
            categories=normalized_categories,
            start=start,
            max_results=max_results,
            retrieved_at=retrieved_at,
            total_results=total_results,
            returned_results=len(records),
        )
        return ArxivSearchPage(records=records, provenance=provenance)
