# AST-RI RI-01 — Literature Source Registry

**Status:** Initial implementation  
**Version:** 0.2.0  
**Scope:** Bibliographic metadata for theoretical-physics literature only

RI-01 is a local SQLite registry for bibliographic metadata. It is not a paper reader or a scientific reasoning system. Provider connectors retrieve metadata only; they do not download or retain article full text or abstracts.

## Current capabilities

- Store title, authors, source type, year, publication date, DOI, arXiv ID, and URL.
- Normalize DOI and arXiv identifiers.
- Generate deterministic source IDs and reject duplicate identifiers.
- Retrieve and search local source records.
- Fetch an arXiv record by arXiv ID.
- Resolve a DOI through Crossref.
- Preserve provider name, provider record ID, retrieval timestamp, and a metadata snapshot.
- Report disagreements between provider records without silently choosing a winner.
- Run unit tests using mocked HTTP responses and no live network access.

## Install

From this directory:

```bash
python -m pip install -e .
```

No third-party runtime dependencies are required.

## Example: retrieve metadata

```python
from ast_ri_source_registry import ArxivProvider, CrossrefProvider

arxiv_record = ArxivProvider().fetch_by_id("2301.01234")
crossref_record = CrossrefProvider().fetch_by_doi("10.1000/example")
```

Use real identifiers when running this example. Provider calls require an internet connection.

## Example: persist provenance

```python
from ast_ri_source_registry import SourceRegistry

registry = SourceRegistry("data/theoretical_physics.sqlite3")
registry.add_source(arxiv_record.source)
registry.add_provider_record(arxiv_record)
print(registry.provider_records(arxiv_record.source.source_id))
```

A provider snapshot can only be attached to an existing canonical source. If two providers return records with different generated source IDs, reconcile identity explicitly before attaching both snapshots. The library does not automatically assume that similar titles refer to the same work.

## Compare provider records

```python
from ast_ri_source_registry import compare_provider_records

conflicts = compare_provider_records([arxiv_record, crossref_record])
for field, values in conflicts.items():
    print(field, values)
```

The comparison reports differing values. It does not resolve them or establish which provider is correct.

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Tests use fixed fixture responses and do not call arXiv or Crossref.

## Scope and limitations

- arXiv connector currently retrieves one record by ID; it is not a topic search client.
- Crossref connector currently resolves one DOI; it is not a broad literature-search client.
- Provider metadata is not independently verified by AST-RI.
- A bibliographic record does not imply that a paper has been read, a claim checked, or a result reproduced.
- No claim extraction, equation parsing, assumption analysis, vector search, or AI-generated research is implemented.
- Metadata search and later literature selection must be restricted to AST-RI's theoretical-physics scope; metadata providers themselves are general scholarly services.

## Provenance and data policy

- Store metadata and stable identifiers, not copyrighted paper text.
- Keep provider, provider record ID, and retrieval timestamp alongside each provider snapshot.
- Preserve disagreements for review; never silently overwrite provider values.
- Do not invent missing authors, dates, identifiers, or publication venues.
- Keep metadata provenance separate from the evidence needed to support scientific claims.
