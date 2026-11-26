# AST-RI RI-02 — Claim, Equation, and Assumption Records

**Status:** Initial deterministic prototype  
**Version:** 0.1.0  
**Domain:** Theoretical physics only

RI-02 accepts plain text supplied by the caller and identifies candidate claim sentences and LaTeX equation spans. It also defines a typed, human-authored assumption record that keeps explicit author statements separate from analyst inferences.

This is a transparent extraction and record-keeping aid, not a scientific reasoning or verification engine.

## Install

```bash
python -m pip install -e .
```

Python 3.10+; standard library only.

## Extract claim and equation candidates

```python
from ast_ri_extraction import extract_candidates

paper_text = open("paper.txt", encoding="utf-8").read()
result = extract_candidates(paper_text, source_id="your-ri01-source-id")

for claim in result.claims:
    print(claim.claim_id, claim.locator, claim.text)

for equation in result.equations:
    print(equation.equation_id, equation.locator, equation.latex)

records = result.to_dict()
```

## Record an assumption after human inspection

```python
from ast_ri_extraction import AssumptionKind, AssumptionRecord

explicit = AssumptionRecord.create(
    source_id="your-ri01-source-id",
    statement="The spacetime is assumed to be asymptotically flat.",
    kind=AssumptionKind.EXPLICIT,
    locator="Section 2, paragraph 1",
    evidence_quote="We assume asymptotic flatness.",
    affected_claim_ids=("claim-id-from-review",),
)

inferred = AssumptionRecord.create(
    source_id="your-ri01-source-id",
    statement="The field is differentiable in the region considered.",
    kind=AssumptionKind.INFERRED,
    locator="Page 3, paragraph 2",
    evidence_quote="Taking the second derivative gives...",
    rationale="The operation requires differentiability, but the paper does not state it as a separate assumption.",
)
```

Assumption records are authored by a researcher after inspecting the source; the package does not automatically infer assumptions. Both types require a source locator and supporting quotation. Inferred assumptions additionally require a rationale. The label `explicit` means the author states the condition; it does not mean the condition is justified or physically correct. Both types start as unreviewed.

## What candidate extraction does

- **Claim candidates:** sentences containing a small, explicit set of linguistic cues such as "we show", "we prove", "we derive", "we find", "it follows that", and numbered theorem/proposition references.
- **Equation candidates:** LaTeX display delimiters `\\[...\\]`, `$$...$$`, inline delimiters `\\(...\\)`, and common equation/alignment environments.

The cue list is intentionally conservative and incomplete. A sentence without a cue may still contain an important scientific claim; a sentence with a cue may not be a substantive or correct claim. These outputs are candidates for review, not a complete inventory.

## Provenance contract

- `source_id` is supplied by the caller and should refer to an RI-01 source record.
- Offsets are zero-based, end-exclusive Python character offsets into the exact supplied string.
- Line numbers are one-based.
- The document digest is SHA-256 over the exact UTF-8 input.
- Claim/equation IDs are deterministic for a given source ID, span text, and offset.
- Original LaTeX spans are preserved; no normalization or symbolic rewriting occurs.
- Claim records start with `epistemic_status="unclassified_candidate"`.
- Equation records start with `transcription_status="not_verified"`.
- Assumption records preserve the explicit/inferred distinction, evidence quote, locator, rationale, and affected claim IDs.

## Important limitations

- Input is plain text only. This package does not download papers, parse PDFs, perform OCR, or recover page numbers.
- Upstream PDF/text conversion must preserve a page-to-text mapping separately if page-level citations are required.
- Sentence splitting and linguistic cue matching are heuristic; they can miss claims and produce false positives.
- LaTeX extraction only recognizes the documented delimiters/environments. It does not recover equations embedded as images or non-LaTeX typography.
- Assumptions are human-authored records, not machine-generated conclusions.
- No equation is parsed, simplified, dimension-checked, or verified.
- No claim is assessed for truth, novelty, proof validity, or empirical support.
- No language model is required or called.

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The test suite uses fixed text fixtures and does not access external services.
