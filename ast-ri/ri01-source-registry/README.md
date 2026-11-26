# AST-RI RI-01 — Literature Source Registry

**Status:** Initial implementation with constrained search and human review  
**Version:** 0.3.0  
**Scope:** Bibliographic metadata for theoretical-physics literature only

RI-01 is a local SQLite registry for bibliographic metadata. It is not a paper reader or a scientific reasoning system. Provider connectors retrieve metadata only; they do not download or retain article full text or abstracts.

## Current capabilities

- Store title, authors, source type, year, publication date, DOI, arXiv ID, and URL.
- Normalize DOI and arXiv identifiers.
- Generate deterministic source IDs and reject duplicate identifiers.
- Retrieve and search local source records.
- Fetch an arXiv record by arXiv ID and resolve a DOI through Crossref.
- Search arXiv with pagination, bounded result counts, sorting, and query provenance.
- Restrict arXiv search to the explicit AST-RI category allowlist: `hep-th`, `gr-qc`, `math-ph`, and `quant-ph`.
- Preserve provider name, provider record ID, retrieval timestamp, and metadata snapshots.
- Report disagreements between provider records without silently choosing a winner.
- Maintain an append-only, human-authored relevance-review history.
- Place unreviewed records in the `uncertain` queue by default.
- Run unit tests using mocked HTTP responses and no live provider calls.

## Install

From this directory:

```bash
python -m pip install -e .
```

No third-party runtime dependencies are required.

## Example: search theoretical-physics literature

```python
from ast_ri_source_registry import ArxivSearchProvider

provider = ArxivSearchProvider()
page = provider.search(
    "causal set quantum gravity",
    categories=("gr-qc", "hep-th", "math-ph"),
    start=0,
    max_results=25,
    sort_by="relevance",
)

for result in page.records:
    print(result.source.title, result.source.arxiv_id)

# Retain this alongside the imported records for reproducibility.
print(page.provenance)
```

The client constructs a category-bounded query and treats the user's search text as a literal phrase. Categories outside the explicit allowlist are rejected. The default maximum is 25; the hard per-request maximum is 100. Use `start` to request subsequent pages. The returned total is the provider-reported result count, not a count of records independently verified by AST-RI.

The allowlist is a discovery filter, not an automatic relevance classifier. A paper in one of these categories can still be outside AST-RI's research scope, and relevant work may be classified elsewhere. Review each candidate before treating it as in scope.

## Example: register a source and review relevance

```python
from ast_ri_source_registry import (
    ArxivSearchProvider,
    RelevanceReviewStore,
    RelevanceStatus,
    SourceRegistry,
)

registry = SourceRegistry("data/theoretical_physics.sqlite3")
page = ArxivSearchProvider().search("black hole information", ["gr-qc", "hep-th"])

for result in page.records:
    try:
        registry.add_source(result.source)
    except ValueError:
        # Duplicate identifiers require explicit reconciliation.
        continue

reviews = RelevanceReviewStore(registry)
queue = reviews.list_queue(registry)  # unreviewed defaults to UNCERTAIN

# After a human has inspected the source:
candidate = queue[0]
reviews.record_review(
    candidate.source.source_id,
    RelevanceStatus.IN_SCOPE,
    rationale="The paper's central subject is a theoretical quantum-gravity model.",
    assessor="reviewer-id",
)
```

Review history is append-only. The latest review determines the current queue status, while earlier decisions remain in the database. Valid labels are `in_scope`, `uncertain`, and `out_of_scope`. A category match never changes a record's relevance status automatically.

## Existing metadata connectors

```python
from ast_ri_source_registry import ArxivProvider, CrossrefProvider

arxiv_record = ArxivProvider().fetch_by_id("2301.01234")
crossref_record = CrossrefProvider().fetch_by_doi("10.1000/example")
```

Use real identifiers when running this example. Provider calls require an internet connection.

## Provenance and provider disagreements

Provider snapshots retain provider name, provider record ID, retrieval time, and metadata. If two providers return records with different generated source IDs, reconcile identity explicitly before attaching both snapshots. The library does not automatically assume that similar titles refer to the same work.

`compare_provider_records` reports differing field values. It does not resolve them or establish which provider is correct.

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Tests use fixed fixture responses and do not call arXiv or Crossref.

## Scope and limitations

- Search currently uses arXiv metadata only; Crossref remains a DOI-resolution connector, not a broad search client.
- The allowlist is deliberately narrow and does not cover every potentially relevant theoretical-physics subfield.
- arXiv categories are search constraints, not proof of theoretical-physics relevance.
- Search results require human relevance review; the default status is `uncertain`.
- Provider metadata and reported result counts are not independently verified by AST-RI.
- A bibliographic record does not imply that a paper has been read, a claim checked, or a result reproduced.
- No claim extraction, equation parsing, assumption analysis, vector search, or AI-generated research is implemented.

## Provenance and data policy

- Store metadata and stable identifiers, not copyrighted paper text.
- Preserve query text, selected categories, pagination offset, result count, and retrieval timestamp.
- Keep provider, provider record ID, and retrieval timestamp alongside each provider snapshot.
- Preserve disagreements and review history; never silently overwrite them.
- Do not invent missing authors, dates, identifiers, or publication venues.
- Keep metadata provenance separate from the evidence needed to support scientific claims.
