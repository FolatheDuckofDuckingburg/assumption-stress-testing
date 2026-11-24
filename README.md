# AST

### Assumption Stress Testing

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--2148--5675-green.svg)](https://orcid.org/0009-0007-2148-5675)

**AST (Assumption Stress Testing) is an independent theoretical physics research initiative.** It investigates the mathematical foundations and assumptions of physical theories, reproduces established results, and examines the consistency and consequences of carefully specified changes to theoretical assumptions.

AST approaches these questions as mathematical physics: through equations, geometry, derivations, proofs, models, computation where appropriate, and physical interpretation. Philosophical discussion may clarify a question, but it does not substitute for mathematical or physical analysis.

## Research scope

AST's areas of interest include:

- **General relativity and gravitation:** spacetime geometry, Einstein's field equations, gravitational dynamics, and exact or approximate solutions.
- **Black-hole physics:** black-hole spacetimes, horizons, geodesics, orbital dynamics, and related physical properties.
- **Causal set theory:** discrete spacetime models, causal order, local finiteness, continuum approximation, and the relationship between causal structure and geometry.
- **Quantum gravity:** mathematical approaches to the relationship between quantum theory and gravitation.
- **Cosmology:** spacetime dynamics, cosmological models, and the large-scale structure and evolution of the universe.
- **Theoretical particle physics:** fundamental particles, interactions, gauge symmetries, the Standard Model, phenomenology, and carefully specified extensions.
- **Quantum field theory:** the mathematical framework of quantum fields, quantization, gauge theories, renormalization, and effective field theory.
- **Mathematical physics:** the mathematical methods and structures used to formulate and investigate physical theories.
- **String theory and related frameworks:** their mathematical formulation, consistency conditions, and physical implications.

These are research directions, not claims of expertise or completed results. Each investigation must define its question, scope, prerequisites, and evidential status.

## Research approach

AST investigates established theories carefully before attempting to generalize them. A typical investigation may:

1. Define a physical question and identify the theory and regime in which it is posed.
2. Review relevant literature and reproduce established results.
3. State mathematical assumptions, conventions, and boundary or initial conditions.
4. Derive relevant equations and consequences analytically.
5. Use symbolic or numerical computation where it provides a useful check or enables analysis.
6. Examine mathematical consistency, limiting cases, stability, and physical interpretation.
7. Identify observable or otherwise discriminating consequences where applicable.
8. Report what was established, what remains conjectural, and what failed.

The methods must fit the physics being studied; not every investigation will follow the same sequence.

## Research standards

- **Mathematical rigor:** define symbols, assumptions, units, conventions, and domains of validity.
- **Engagement with existing work:** compare claims with established literature and known results.
- **Correspondence:** a proposed extension should recover established results in regimes where those results are experimentally supported, unless the study explicitly concerns a different regime.
- **Consistency:** check equations, limiting behaviour, symmetries, conservation laws, and relevant stability conditions.
- **Empirical accountability:** distinguish mathematical possibility from physical evidence.
- **Reproducibility:** preserve derivations, code, parameters, references, and computational procedures.
- **Intellectual honesty:** negative results, unresolved questions, and corrections are valid research outcomes.

AST does not presume that established theories are wrong. Stress-testing an assumption may show that it is essential, that a theory is robust to its relaxation, or that a proposed change creates inconsistencies. Mathematical consistency alone does not establish physical truth, and novelty is not established merely by changing an assumption or obtaining a different equation.

## Research organization

- [Research charter](research/charter/RESEARCH_CHARTER.md) — scope, standards, and operating principles.
- [General relativity](research/general_relativity/README.md) — relativistic gravitation and spacetime geometry.
- [Black-hole physics](research/black_hole_physics/README.md) — black-hole spacetimes and their physical properties.
- [Causal set theory](research/causal_set_theory/README.md) — discrete spacetime and causal structure.
- [Quantum gravity](research/quantum_gravity/README.md) — approaches to quantum descriptions of gravitation.
- [Cosmology](research/cosmology/README.md) — theoretical models of the universe and its evolution.
- [Theoretical particle physics](research/theoretical_particle_physics/README.md) — particle models, symmetries, interactions, and phenomenology.
- [Quantum field theory](research/quantum_field_theory/README.md) — mathematical foundations and methods for quantum fields.
- [AST-GR-001](research/general_relativity/AST-GR-001_SCHWARZSCHILD.md) — foundational study of Schwarzschild spacetime and geodesic structure.

## Initial research milestone

### AST-GR-001 — Schwarzschild Spacetime: Mathematical Foundations and Geodesic Structure

The first study establishes a reliable foundation in the Schwarzschild solution before any proposed extension is considered. It examines the metric, curvature, timelike and null geodesics, circular orbits, the photon sphere, and the innermost stable circular orbit (ISCO).

The initial objective is reproduction and understanding of established results, not a claim of novelty. See the [study specification](research/general_relativity/AST-GR-001_SCHWARZSCHILD.md).

## Existing computational and formal work

The repository's earlier computational and formal-methods work remains part of AST's development history. It is methodological groundwork and must be interpreted within the scope of the experiments and formal statements actually implemented.

The earlier synthetic graph-recovery experiment is a computational methods prototype. It is not evidence that spacetime emerges from information, does not establish a physical metric, and does not constitute a theory of gravity.

The initial Lean 4 formalization explores finite contexts of propositions, entailment, weakening, and basic propositional reasoning. Formal verification checks proofs relative to encoded definitions and premises; it does not establish that physical premises are true or empirically adequate. See [docs/FORMALIZATION.md](docs/FORMALIZATION.md).

## Research status

AST is an independent, developing research initiative. The topics listed above are areas of intended investigation, not completed research results. AST-GR-001 begins with established general relativity as a foundational study. Any later proposal of a new or generalized physical model will require a precise mathematical formulation, derivation, consistency analysis, comparison with prior work, and a defensible account of its physical implications.

## Repository map

```text
research/
├── charter/
├── general_relativity/
├── black_hole_physics/
├── causal_set_theory/
├── quantum_gravity/
└── cosmology/

docs/
formal/
[existing computational code and tests]
```

The directory structure will grow as actual studies and reproducible materials are added. A directory or research brief does not imply that a result has been derived or validated. Existing computational code and tests are retained as exploratory methodological work.

## Reproducibility and interpretation

For computational work, record software versions, parameters, random seeds, numerical methods, and evaluation procedures where relevant. For analytical work, record definitions, assumptions, intermediate steps, conventions, and references.

Software tests establish properties of an implementation; they do not validate a physical hypothesis. Numerical agreement with a known result is a verification step, not automatically a novel contribution.

## License

This project is distributed under the [Apache License 2.0](LICENSE).

## Author

**Folarera Kassim**

[ORCID: 0009-0007-2148-5675](https://orcid.org/0009-0007-2148-5675)
