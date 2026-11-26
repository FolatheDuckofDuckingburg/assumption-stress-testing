"""Metadata-only clients for arXiv and Crossref.

The clients retrieve bibliographic metadata only. They never download paper
full text. Network access is isolated behind an injectable transport so tests
can use deterministic fixtures.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re
import time
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from .models import Source, SourceType, normalize_arxiv_id, normalize_doi


class ProviderError(RuntimeError):
    """Raised when a metadata provider cannot return a valid record."""


Transport = Callable[[str, dict[str, str], float], bytes]


def _default_transport(url: str, headers: dict[str, str], timeout: float) -> bytes:
    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def _retrieved_at() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass(frozen=True, slots=True)
class ProviderRecord:
    """A normalized source plus provider-specific provenance."""

    source: Source
    provider: str
    provider_record_id: str
    retrieved_at: str


class MetadataProvider:
    provider_name = "abstract"

    def __init__(
        self,
        transport: Transport | None = None,
        timeout: float = 15.0,
        max_retries: int = 2,
        user_agent: str = "AST-RI/0.1 (metadata research client)",
    ) -> None:
        if timeout <= 0:
            raise ValueError("timeout must be positive.")
        if max_retries < 0:
            raise ValueError("max_retries must be non-negative.")
        self.transport = transport or _default_transport
        self.timeout = timeout
        self.max_retries = max_retries
        self.headers = {
            "User-Agent": user_agent,
            "Accept": "application/atom+xml, application/json",
        }

    def _get(self, url: str) -> bytes:
        for attempt in range(self.max_retries + 1):
            try:
                return self.transport(url, self.headers, self.timeout)
            except HTTPError as exc:
                if exc.code == 429 or 500 <= exc.code < 600:
                    if attempt < self.max_retries:
                        time.sleep(min(2 ** attempt, 4))
                        continue
                raise ProviderError(
                    f"{self.provider_name} returned HTTP {exc.code}."
                ) from exc
            except (URLError, TimeoutError) as exc:
                if attempt < self.max_retries:
                    time.sleep(min(2 ** attempt, 4))
                    continue
                raise ProviderError(
                    f"Could not reach {self.provider_name}: {exc}"
                ) from exc
        raise ProviderError(f"{self.provider_name} request failed.")


class ArxivProvider(MetadataProvider):
    """Fetch a single arXiv record by its stable identifier."""

    provider_name = "arxiv"
    API_URL = "https://export.arxiv.org/api/query"

    def fetch_by_id(self, arxiv_id: str) -> ProviderRecord:
        normalized = normalize_arxiv_id(arxiv_id)
        query = urlencode({"id_list": normalized})
        payload = self._get(f"{self.API_URL}?{query}")
        try:
            root = ET.fromstring(payload)
        except ET.ParseError as exc:
            raise ProviderError("arXiv returned malformed Atom XML.") from exc

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            raise ProviderError(f"No arXiv record found for {normalized}.")

        title = " ".join((entry.findtext("atom:title", default="", namespaces=ns)).split())
        author_names = [
            " ".join((node.text or "").split())
            for node in entry.findall("atom:author/atom:name", ns)
        ]
        published = entry.findtext("atom:published", default="", namespaces=ns)
        published_date = published[:10] if published else None
        doi = entry.findtext("atom:doi", default=None, namespaces=ns)
        summary = entry.findtext("atom:summary", default="", namespaces=ns)
        del summary  # Abstract text is deliberately not stored by RI-01.1.

        if not title or not author_names:
            raise ProviderError("arXiv record is missing a title or authors.")

        year = int(published_date[:4]) if published_date else None
        source = Source(
            title=title,
            authors=tuple(author_names),
            source_type=SourceType.PREPRINT,
            year=year,
            published_date=published_date,
            doi=doi,
            arxiv_id=normalized,
            url=f"https://arxiv.org/abs/{normalized}",
        )
        return ProviderRecord(
            source=source,
            provider=self.provider_name,
            provider_record_id=normalized,
            retrieved_at=_retrieved_at(),
        )


class CrossrefProvider(MetadataProvider):
    """Resolve a DOI to Crossref bibliographic metadata."""

    provider_name = "crossref"
    API_URL = "https://api.crossref.org/works/"

    def fetch_by_doi(self, doi: str) -> ProviderRecord:
        normalized = normalize_doi(doi)
        payload = self._get(f"{self.API_URL}{quote(normalized, safe='/')}")
        try:
            response = json.loads(payload.decode("utf-8"))
            item = response["message"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise ProviderError("Crossref returned malformed metadata JSON.") from exc

        titles = item.get("title") or []
        title = titles[0].strip() if titles and isinstance(titles[0], str) else ""
        authors = []
        for author in item.get("author") or []:
            given = (author.get("given") or "").strip()
            family = (author.get("family") or "").strip()
            name = " ".join(part for part in (given, family) if part)
            if name:
                authors.append(name)

        if not title or not authors:
            raise ProviderError("Crossref record is missing a title or authors.")

        date_parts = (
            item.get("published-print", {}).get("date-parts")
            or item.get("published-online", {}).get("date-parts")
            or item.get("created", {}).get("date-parts")
            or []
        )
        published_date = None
        year = None
        if date_parts and date_parts[0]:
            parts = date_parts[0]
            year = int(parts[0])
            if len(parts) >= 3:
                published_date = f"{int(parts[0]):04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
            elif len(parts) == 2:
                published_date = f"{int(parts[0]):04d}-{int(parts[1]):02d}-01"
            else:
                published_date = f"{int(parts[0]):04d}-01-01"

        url = item.get("URL") or f"https://doi.org/{normalized}"
        source = Source(
            title=title,
            authors=tuple(authors),
            source_type=SourceType.JOURNAL_ARTICLE,
            year=year,
            published_date=published_date,
            doi=normalized,
            url=url,
        )
        return ProviderRecord(
            source=source,
            provider=self.provider_name,
            provider_record_id=normalized,
            retrieved_at=_retrieved_at(),
        )


def compare_provider_records(
    records: list[ProviderRecord],
) -> dict[str, tuple[str, ...]]:
    """Return fields with distinct provider values; never pick a winner."""
    if len(records) < 2:
        return {}
    fields = ("title", "authors", "year", "published_date", "doi", "arxiv_id")
    conflicts: dict[str, tuple[str, ...]] = {}
    for field in fields:
        values = []
        for record in records:
            value = getattr(record.source, field)
            if value is None:
                continue
            rendered = " | ".join(value) if field == "authors" else str(value)
            if rendered not in values:
                values.append(rendered)
        if len(values) > 1:
            conflicts[field] = tuple(values)
    return conflicts
