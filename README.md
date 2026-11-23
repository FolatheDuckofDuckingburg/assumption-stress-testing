# AST

### Theoretical Physics Research

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--2148--5675-green.svg)](https://orcid.org/0009-0007-2148-5675)

**AST is an independent theoretical physics research initiative.** Its work focuses on the mathematical foundations of physical theories, rigorous theoretical derivation, analysis of physical models, and the investigation of possible generalizations or extensions.

AST is the project's name. It is not expanded into a formal acronym.

The research programme is broad in scope. It may investigate established frameworks, unresolved theoretical questions, and candidate models, provided each study is mathematically explicit and appropriately grounded in existing physics.

## Research scope

Areas of interest include:

- **General relativity and gravitation:** spacetime geometry, Einstein's field equations, black holes, gravitational dynamics, and exact or approximate solutions.
- **Quantum gravity:** conceptual and mathematical approaches to the relationship between quantum theory and gravitation.
- **Cosmology:** spacetime evolution, cosmological models, and the mathematical foundations of large-scale physical descriptions.
- **Quantum field theory and particle physics:** field-theoretic structures, symmetries, interactions, and candidate extensions.
- **Mathematical physics:** differential geometry, analysis, algebraic structures, and mathematical methods used to formulate physical theories.

These are research directions, not claims of expertise or completed results. Individual studies will define their own scope and prerequisites.

## Research approach

AST investigates physical theories through a repeatable mathematical process:

1. **Specify the theory and regime.** Identify the physical system, governing framework, assumptions, approximations, and domain of applicability.
2. **Formulate the question.** State a precise theoretical problem that can be addressed mathematically.
3. **Establish the baseline.** Derive or reproduce relevant established results before proposing changes.
4. **Develop the analysis.** Use analytical derivation, mathematical proof, and—where useful—symbolic or numerical computation.
5. **Check consistency.** Examine dimensions, limiting cases, symmetries, conservation laws, regularity, stability, and other constraints relevant to the model.
6. **Extract physical consequences.** Identify what the mathematics implies for observables, physical interpretation, or the structure of the theory.
7. **Compare with established physics.** Determine which known results must be recovered and what evidence would be needed to distinguish a proposed extension.
8. **Report limitations.** Separate established results, derived results, numerical evidence, conjectures, and open questions.

AST does not assume that established theories are wrong. A successful theory may be incomplete without being invalid in its tested regime. Mathematical consistency is necessary for a viable model, but it is not by itself evidence that the model describes nature.

## First investigation: Schwarzschild spacetime

The initial research milestone is:

**AST-GR-001 — Schwarzschild Spacetime: Mathematical Foundations and Geodesic Structure**

This study begins with the Schwarzschild solution of general relativity and examines the geometry and motion it describes. Planned topics include:

- The Schwarzschild metric and its coordinate interpretation.
- Curvature and geometric properties of the spacetime.
- Timelike and null geodesics.
- Circular orbits and their stability.
- The photon sphere and innermost stable circular orbit (ISCO).
- Limiting cases and consistency checks against established results.

The first objective is reproduction and understanding, not novelty. Any later modification or extension must be motivated, derived explicitly, and tested against the Schwarzschild baseline and relevant physical constraints.

See [the AST-GR-001 research brief](research/investigations/AST-GR-001/README.md).

## Existing computational and formal work

The repository's earlier computational and formal-methods work remains part of AST's research history.

### Synthetic graph-recovery benchmark

The existing synthetic graph-recovery experiment investigates whether a planted graph structure can be recovered from samples of a Gaussian model using pairwise mutual-information estimates and a top-neighbour inference rule. It is a methodological computational experiment with a known synthetic reference structure.

**Scope limitation:** graph recovery in this synthetic setting does not demonstrate spacetime emergence, establish a physical metric, or provide evidence for a theory of gravity. It is not a physical result.

### Lean 4 formalization

The initial Lean 4 module explores finite contexts of propositions, entailment, weakening, and basic propositional reasoning. It is a small formal-methods scaffold. It does not establish the physical truth of premises or the empirical adequacy of a physical theory.

See [docs/FORMALIZATION.md](docs/FORMALIZATION.md) for its documented scope and limitations.

## Research standards

AST follows these standards:

- **Mathematical explicitness:** definitions, assumptions, conventions, and derivations must be inspectable.
- **Respect for established results:** reproduce relevant baselines and account for verified predictions.
- **Physical motivation:** do not alter a theory merely to generate mathematical novelty.
- **Consistency before interpretation:** check mathematical and physical constraints before assigning meaning to a result.
- **Evidence-aware claims:** distinguish mathematical possibility from physical plausibility and empirical support.
- **Reproducibility:** document derivations, code, parameters, numerical methods, and sources where applicable.
- **Honest reporting:** negative results, failed approaches, and unresolved questions are legitimate research outcomes.

## Repository map

The repository is being organized around the following research areas:

- `research/charter/` — scope, standards, and research governance.
- `research/general_relativity/` — general-relativity research notes and studies.
- `research/investigations/` — individually scoped research investigations.
- `docs/` — project documentation and methodological notes.
- `formal/` — Lean 4 formalization work.
- Existing computational code and tests — retained as exploratory methodological work.

The directory structure will grow as actual studies and reproducible materials are added. A directory or research brief does not imply that a result has been derived or validated.

## Reproducibility and interpretation

For computational work, record software versions, parameters, random seeds, numerical methods, and evaluation procedures where relevant. For analytical work, record definitions, assumptions, intermediate steps, conventions, and references.

Software tests establish properties of an implementation; they do not validate a physical hypothesis. Numerical agreement with a known result is a verification step, not automatically a novel contribution.

## License

This project is distributed under the [Apache License 2.0](LICENSE).

## Author

**Folarera Kassim**

[ORCID: 0009-0007-2148-5675](https://orcid.org/0009-0007-2148-5675)
