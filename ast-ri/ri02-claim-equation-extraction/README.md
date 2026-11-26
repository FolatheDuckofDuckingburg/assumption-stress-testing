# AST-RI RI-02 — Claim and Equation Extraction

**Status:** Initial deterministic prototype  
**Version:** 0.1.0  
**Domain:** Theoretical physics only

RI-02 accepts plain text supplied by the caller and identifies candidate claim sentences and LaTeX equation spans. It preserves exact text, character offsets, line numbers, a SHA-256 digest of the input, and a stable source identifier.

This is a transparent extraction aid, not a scientific reasoning or verification engine.

## Install

```bash
python -m pip install -e .
```

Python 3.10+; standard library only.

## Example

```python
from ast_ri_extraction import extract_candidates

paper_text = open("paper.txt", encoding="utf-8").read()
result = extract_candidates(paper_text, source_id="your-ri01-source-id")

for claim in result.claims:
    print(claim.claim_id, claim.locator, claim.text)

for equation in result.equations:
    print(equation.equation_id, equation.locator, equation.latex)

# JSON-serializable structure for a review queue or evidence ledger:
records = result.to_dict()
```

## What it extracts

- **Claim candidates:** sentences containing a small, explicit set of linguistic cues such as "we show", "we prove", "we derive", "we find", "it follows that", and numbered theorem/proposition references.
- **Equation candidates:** LaTeX display delimiters `\\[...\\]`, `$$...$$`, inline delimiters `\\(...\\)`, and common equation/alignment environments.

The cue list is intentionally conservative and incomplete. A sentence without a cue may still contain an important scientific claim; a sentence with a cue may not be a substantive or correct claim. These outputs are candidates for review, not a complete inventory.

## Provenance contract

- `source_id` is supplied by the caller and must refer to an existing RI-01 source record.
- Offsets are zero-based, end-exclusive Python character offsets into the exact supplied string.
- Line numbers are one-based.
- The document digest is SHA-256 over the exact UTF-8 input.
- Claim/equation IDs are deterministic for a given source ID, span text, and offset.
- Original LaTeX spans are preserved; no normalization or symbolic rewriting occurs.
- Every record starts with `review_status="unreviewed"`.
- Claims start with `epistemic_status="unclassified_candidate"`.
- Equations start with `transcription_status="not_verified"`.

## Important limitations

- Input is plain text only. This package does not download papers, parse PDFs, perform OCR, or recover page numbers.
- Upstream PDF/text conversion must preserve a page-to-text mapping separately if page-level citations are required.
- Sentence splitting and linguistic cue matching are heuristic; they can miss claims and produce false positives.
- LaTeX extraction only recognizes the documented delimiters/environments. It does not recover equations embedded as images or non-LaTeX typography.
- No assumptions are inferred or classified in this milestone.
- No equation is parsed, simplified, dimension-checked, or verified.
- No claim is assessed for truth, novelty, proof validity, or empirical support.
- No language model is required or called.

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The test suite uses fixed text fixtures and does not access external services.
