# AST

### Assumption Stress Testing

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--2148--5675-green.svg)](https://orcid.org/0009-0007-2148-5675)

**AST is an independent theoretical physics research initiative.** Its work focuses on the mathematical foundations of physical theories, rigorous theoretical derivation, the development and analysis of physical models, and the investigation of possible generalizations of established theories.

The programme is intended to engage with theoretical physics as physics: mathematical structures, field equations, spacetime geometry, dynamical systems, physical interpretation, and consequences that can in principle be compared with observation. Philosophical discussion may clarify a problem, but it is not a substitute for mathematical or physical work.

## Research scope

AST is broad in scope. Areas of interest include:

- **General relativity:** spacetime geometry, Einstein's field equations, gravitational dynamics, and exact or approximate solutions.
- **Black-hole physics:** horizons, geodesics, orbital dynamics, thermodynamics, and related questions.
- **Quantum gravity:** mathematical approaches to the relationship between quantum theory and gravitation.
- **Cosmology:** spacetime dynamics, cosmological models, and the large-scale structure and evolution of the universe.
- **Quantum field theory and particle physics:** field-theoretic structures, symmetries, interactions, and model analysis.
- **Mathematical physics:** the mathematical methods and structures used to formulate and investigate physical theories.
- **String theory and related frameworks:** studied through their mathematical formulation, consistency conditions, and physical implications.

This list describes research interests, not completed results or claims of expertise. Individual investigations will have explicitly bounded questions and prerequisites.

## Research approach

AST investigates established theories carefully before attempting to generalize them. A typical study may:

1. Define a physical question and identify the theory and regime in which it is posed.
2. Review the relevant literature and reproduce established results.
3. State the mathematical assumptions, conventions, and boundary or initial conditions.
4. Derive the relevant equations and consequences analytically.
5. Use symbolic or numerical computation where it provides a useful check or enables analysis.
6. Examine mathematical consistency, limiting cases, stability, and physical interpretation.
7. Identify observable or otherwise discriminating consequences where applicable.
8. Report what was established, what remains conjectural, and what failed.

Not every investigation will follow this sequence exactly. The methods must fit the physics being studied.

## Research standards

- **Mathematical rigor:** define symbols, assumptions, units, conventions, and domains of validity.
- **Engagement with existing work:** compare claims with established literature and known results.
- **Correspondence:** a proposed extension must recover established results in regimes where those results are experimentally supported, unless the study explicitly examines a different regime.
- **Consistency:** check equations, limiting behaviour, symmetries, conservation laws, and relevant stability conditions.
- **Empirical accountability:** distinguish mathematical possibility from physical evidence.
- **Reproducibility:** preserve derivations, code, parameters, references, and computational procedures.
- **Intellectual honesty:** negative results, unresolved questions, and corrections are valid research outcomes.

AST does not presume that established theories are wrong. Mathematical consistency alone does not establish physical truth, and novelty is not established merely by changing an assumption or obtaining a different equation.

## Research organization

- [Research charter](research/charter/RESEARCH_CHARTER.md) — scope, standards, and operating principles.
- [General relativity](research/general_relativity/README.md) — investigations of relativistic gravitation and spacetime geometry.
- [Black-hole physics](research/black_hole_physics/README.md) — black-hole spacetimes and their physical properties.
- [Quantum gravity](research/quantum_gravity/README.md) — approaches to quantum descriptions of gravitation.
- [Cosmology](research/cosmology/README.md) — theoretical models of the universe and its evolution.
- [AST-GR-001](research/general_relativity/AST-GR-001_SCHWARZSCHILD.md) — first study: Schwarzschild spacetime and geodesic structure.

## Initial research milestone

### AST-GR-001 — Schwarzschild Spacetime: Mathematical Foundations and Geodesic Structure

The first study establishes a reliable foundation in the Schwarzschild solution before any proposed extension is considered. It will examine the metric, curvature, timelike and null geodesics, circular orbits, the photon sphere, and the innermost stable circular orbit (ISCO).

The initial objective is reproduction and understanding of established results, not a claim of novelty. See the [study specification](research/general_relativity/AST-GR-001_SCHWARZSCHILD.md).

## Existing computational and formal work

The repository's earlier computational and formal-methods work remains part of AST's development history. It is methodological groundwork and should be interpreted within the scope of the experiments and formal statements actually implemented.

In particular, the earlier synthetic graph-recovery experiment is a computational methods prototype. It is not evidence that spacetime emerges from information, does not establish a physical metric, and does not constitute a theory of gravity.

The initial Lean 4 formalization explores finite contexts of propositions, entailment, weakening, and basic propositional reasoning. Formal verification checks proofs relative to encoded definitions and premises; it does not establish that physical premises are true or empirically adequate. See [docs/FORMALIZATION.md](docs/FORMALIZATION.md).

## Research status

AST is an independent, developing research initiative. The topics listed above are areas of intended investigation; they must not be mistaken for completed research results. AST-GR-001 begins with established general relativity and is a foundational study. Any later proposal of a new or generalized physical model will require a precise mathematical formulation, derivation, consistency analysis, comparison with prior work, and a defensible account of its physical implications.
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
