# AST-RI — Research Intelligence for Theoretical Physics

**Status:** Initial design specification  
**Parent project:** AST (Assumption Stress Testing)  
**Domain:** Theoretical physics only  
**Version:** 0.1.0 (design)

## Mission

AST-RI is an AI-assisted research system for theoretical physics. It is intended to help a researcher inspect the assumptions, mathematical arguments, claims, and open problems found in theoretical-physics literature; trace those items to their sources; and systematically investigate whether a proposed line of reasoning is mathematically and physically defensible.

AST-RI is a research-support tool, not an autonomous physicist. It must not present generated ideas as discoveries, proofs, established results, or physically true claims without the corresponding verification.

## Scope

AST-RI is restricted to theoretical physics and its mathematical foundations. Relevant areas may include:

- General relativity and gravitation
- Black-hole physics and spacetime geometry
- Quantum field theory
- Quantum gravity
- Foundations of quantum mechanics
- Cosmology
- Theoretical particle physics
- Causal set theory
- String theory and related theoretical frameworks
- Mathematical physics directly supporting these areas

A topic list defines the system's permitted research domain; it does not imply that AST-RI has expertise or validated capabilities in every area. Each investigation must declare its specific subdomain, theory, mathematical setting, and regime of validity.

Out of scope: general-purpose scientific discovery, biology, medicine, neuroscience, chemistry, social science, and non-physics research workflows.

## Design principles

1. **Source traceability:** every literature-derived claim must retain a citation and, where available, a page, section, equation, or passage locator.
2. **Separation of epistemic status:** distinguish established results, reproduced results, derivations, numerical outputs, conjectures, hypotheses, and unresolved questions.
3. **Mathematical inspectability:** preserve equations, definitions, assumptions, conventions, derivation steps, and domains of validity.
4. **Baseline before modification:** identify and reproduce relevant established results before testing a proposed change.
5. **Counterargument by design:** actively search for counterexamples, hidden assumptions, limiting cases, and known no-go results.
6. **No novelty inflation:** a generated suggestion is not novel until compared against relevant prior work.
7. **No truth-by-fluency:** language-model confidence or plausibility is not evidence.
8. **Human-verifiable outputs:** prioritize structured research records that a physicist can inspect and independently check.

## Proposed architecture

### 1. Literature and source layer

- Search and ingest permitted theoretical-physics sources.
- Store bibliographic metadata and stable identifiers (DOI, arXiv ID, ISBN, or publisher URL).
- Preserve source text only where licensing and access conditions permit.
- Record exact source locations for extracted claims and equations.
- Distinguish primary papers, reviews, textbooks, and secondary commentary.

### 2. Claim and equation extraction

Represent extracted material as typed records rather than unqualified prose.

Each claim record should include:
- Claim identifier
- Exact or carefully normalized statement
- Source identifier and locator
- Relevant equation or definition, if applicable
- Theory and subdomain
- Assumptions and stated conditions
- Epistemic status
- Extraction method and review status

Automated extraction is provisional until checked against the source.

### 3. Assumption mapping

Build an explicit map connecting:
- A claim or derivation
- Its mathematical and physical assumptions
- Definitions and conventions
- Boundary or initial conditions
- Symmetry and regularity requirements
- Approximation and regime restrictions
- Downstream results that depend on those assumptions

AST-RI must distinguish assumptions explicitly stated by an author from assumptions inferred by the system.

### 4. Stress-testing engine

For a selected claim or derivation, generate a structured audit:

1. Restate the target claim and its source.
2. Enumerate explicit and inferred assumptions separately.
3. Check definitions, dimensions, signs, and conventions.
4. Inspect logical and algebraic steps.
5. Test relevant limiting cases and special cases.
6. Search for counterexamples, incompatibilities, and known constraints.
7. Check symmetries, conservation laws, covariance, causality, stability, or other domain-specific requirements where applicable.
8. Identify what survives, fails, or remains undecided.
9. Cite the evidence for each finding.

The system must not imply that every checklist item applies to every theory. The relevant checks depend on the mathematical and physical setting.

### 5. Mathematical verification layer

Use appropriate tools for symbolic calculations, numerical checks, and formal verification. Record:
- Tool and version
- Inputs and conventions
- Reproducible code or derivation
- Tolerances and numerical settings
- Validation against known results or independent methods
- Limitations of the check

A successful software test is evidence about the implementation, not by itself evidence that a physical theory is correct.

### 6. Research-direction explorer

Generate candidate questions or theoretical directions only after assembling:
- The motivating problem
- Relevant prior work
- The assumptions being examined
- The mathematical change or conjecture being considered
- Expected consequences
- Potential consistency obstacles
- A plan for checking correspondence with established results
- Possible empirical or observational implications, if any

Label all generated directions as **unverified proposals**. Do not label them discoveries or novel contributions.

### 7. Evidence and provenance ledger

Every output should be traceable to one or more of:
- A source passage or equation
- A reproducible derivation
- A computation with recorded settings
- A formal proof with encoded premises
- An explicitly labeled conjecture or inference

If support is absent, say so. Never fabricate citations, equations, page numbers, or validation results.

## Core data model (initial)

The first implementation should use simple, inspectable records.

- **Source:** bibliographic identity, URL or identifier, source type, access/licensing notes.
- **Claim:** statement, source locator, theory, status, reviewer state.
- **Assumption:** statement, explicit/inferred flag, source locator, affected claims.
- **Equation:** LaTeX representation, symbol definitions, source or derivation provenance.
- **Derivation:** ordered steps, premises, transformations, dependencies, verification state.
- **StressTest:** target, test method, assumptions varied, result, limitations, evidence.
- **ResearchQuestion:** motivation, prior work, unknowns, proposed investigation, status.

Use stable identifiers and explicit links between records. Avoid treating unstructured model-generated summaries as the canonical research record.

## Evaluation

AST-RI should be evaluated on bounded tasks with known answers before being used for open-ended research. Initial evaluation dimensions:

- Citation and locator accuracy
- Claim extraction precision and recall
- Correct identification of explicit assumptions
- Correct separation of explicit and inferred assumptions
- Mathematical transcription accuracy
- Reproduction of selected established derivations
- Detection of seeded algebraic or logical errors
- Appropriate identification of inapplicable checks
- Calibration of uncertainty and abstention
- Reproducibility of generated audit records

Evaluation sets must include negative cases where the correct result is that no error is established or that the available evidence is insufficient. Report measured results; do not invent benchmark performance.

## Initial implementation milestones

### RI-00 — Repository and research contract
- Establish this scope and design specification.
- Define record formats and provenance requirements.
- Document licensing and source-handling rules.

### RI-01 — Source registry
- Implement a local bibliographic registry.
- Support stable identifiers and source locators.
- Do not begin with unrestricted bulk scraping.

### RI-02 — Claim and assumption records
- Define validated schemas for sources, claims, assumptions, and equations.
- Add small manually checked examples from openly accessible theoretical-physics material.

### RI-03 — Evidence-linked stress-test reports
- Produce structured reports with explicit assumptions, checks, findings, and citations.
- Include an abstention state when evidence is insufficient.

### RI-04 — Mathematical verification adapters
- Add carefully scoped symbolic or numerical checks.
- Validate against known limiting cases and independent calculations.

### RI-05 — Controlled research-direction exploration
- Generate candidate questions from reviewed evidence maps.
- Require human review and explicit novelty checks.

## Initial technical strategy

Prefer a small, modular Python implementation with typed data models, deterministic validation, and tests. Keep language-model use behind replaceable interfaces. Do not make a particular model provider, vector database, or agent framework a foundational dependency before a concrete requirement is demonstrated.

The first prototype should prioritize provenance and correctness over autonomy or scale.

## Definition of a successful early prototype

Given a small, curated set of theoretical-physics sources and one bounded question, AST-RI can create a reviewable evidence map containing claims, assumptions, equations, and source locations; perform a limited, explicit stress-test; and produce a report that separates supported findings from uncertainty and unverified proposals.

This is a software and research-method milestone. It is not a claim that AST-RI has discovered new physics.

## Relationship to AST

AST is the parent theoretical-physics research initiative and provides the assumption-stress-testing methodology. AST-RI is a proposed software system that operationalizes parts of that methodology for literature-grounded theoretical-physics investigation. The existence of this specification does not imply that the system has been implemented or validated.

## License

This specification is part of the AST repository and is distributed under the repository's Apache License 2.0, subject to the repository's license file.
