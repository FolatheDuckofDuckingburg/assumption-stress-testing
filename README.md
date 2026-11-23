# AST

### Theoretical Physics Research

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--2148--5675-green.svg)](https://orcid.org/0009-0007-2148-5675)

**AST is an independent theoretical physics research initiative.** Its work focuses on the mathematical foundations of physical theories, rigorous theoretical derivation, the development and analysis of physical models, and the investigation of possible generalizations of established theories.

AST is the project name. It is not an acronym that needs to be expanded.

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

## License

This project is distributed under the [Apache License 2.0](LICENSE).

## Author

**Folarera Kassim**

[ORCID: 0009-0007-2148-5675](https://orcid.org/0009-0007-2148-5675)
