# AST-RI RI-01 — Literature Source Registry

**Status:** Initial implementation  
**Version:** 0.1.0  
**Scope:** Bibliographic metadata for theoretical-physics literature only

RI-01 provides a small local SQLite registry for sources that may later support AST-RI's literature-grounded claim and assumption analysis. It is a metadata store, not a literature-search engine, paper reader, or scientific reasoning system.

## Current capabilities

- Store title, author list, source type, year, publication date, DOI, arXiv identifier, and URL.
- Normalize DOI and arXiv identifiers before storage and lookup.
- Generate a deterministic source ID from the strongest available identifier.
- Reject duplicate source IDs, DOIs, arXiv identifiers, and URLs.
- Retrieve by source ID, DOI, or arXiv ID.
- Search titles and author metadata.
- Persist records in a local SQLite database.
- Run unit tests without network access or third-party runtime dependencies.

## Not implemented

- arXiv or Crossref API clients
- Automated metadata enrichment
- Full-text download, parsing, or indexing
- Claim, equation, or assumption extraction
- Vector search, language-model analysis, or autonomous research

These are intentionally separate future capabilities. A record in this registry is not evidence that its paper has been read, reviewed, or verified.

## Installation

From this directory:

```bash
python -m pip install -e .
```

## Example

```python
from ast_ri_source_registry import Source, SourceRegistry, SourceType

registry = SourceRegistry("data/theoretical_physics.sqlite3")

source = Source(
    title="Example paper title",
    authors=("A. Author", "B. Author"),
    year=2024,
    doi="10.1234/example.doi",
    arxiv_id="2401.01234",
    source_type=SourceType.PREPRINT,
)

registry.add_source(source)
print(source.source_id)
print(registry.find_by_arxiv_id("2401.01234"))
```

The example identifiers above are illustrative placeholders, not a real citation.

## Tests

The test suite uses Python's standard-library `unittest`; no test extra is required:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Data and provenance policy

- Store bibliographic metadata and stable identifiers, not paper text.
- Preserve the original DOI/arXiv identity after normalization.
- Do not invent missing authors, dates, identifiers, or publication venues.
- Metadata imported from an external provider must retain its provider and retrieval timestamp in a later ingestion layer.
- A source record does not imply that a claim extracted from the source is correct.
- Full-text handling must be designed separately around copyright, licenses, and access conditions.

## Current implementation boundary

RI-01 is a deterministic local registry. It does not yet connect to arXiv or Crossref, and it does not make claims about the novelty or correctness of any theoretical-physics result.
