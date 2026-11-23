# AST Research Charter

## Identity

AST is an independent theoretical physics research initiative. AST is the project name and is not expanded into a formal acronym.

## Purpose

AST investigates the mathematical foundations and structure of physical theories. Its work may include deriving established results, analyzing open theoretical problems, and developing or assessing candidate generalizations of existing frameworks.

AST is not defined by a single computational technique or by the assumption-testing of theories in isolation. Its central activity is theoretical physics: formulating physical questions mathematically and following their consequences with appropriate rigor.

## Scope

Potential research areas include:

- General relativity and gravitation.
- Black-hole physics and spacetime geometry.
- Quantum gravity.
- Cosmology.
- Quantum field theory and particle physics.
- Mathematical physics and the mathematical structures used throughout these fields.

The scope of each investigation must be narrow enough to support a meaningful derivation and a defensible conclusion.

## Research lifecycle

A study should, where applicable:

1. State a precise physical question.
2. Identify the theory, assumptions, conventions, and regime under consideration.
3. Review relevant established literature and results.
4. Derive or reproduce the baseline mathematics.
5. Develop the proposed analysis or model.
6. Check mathematical consistency and physical constraints.
7. Derive consequences that could, in principle, distinguish the proposal from its baseline.
8. Compare with established observations or explain what evidence would be needed.
9. Document limitations, unresolved issues, and reproducibility information.

Not every project will require every stage in the same form. Deviations should be explained.

## Standards of evidence

AST distinguishes:

- **Established result:** a result supported by the relevant literature and accepted within a stated regime.
- **Reproduced result:** an established result independently derived or computationally recovered in the current study.
- **New derivation:** a result derived in the current work, with assumptions and steps shown.
- **Numerical result:** output from a specified numerical method, subject to its discretization and implementation limitations.
- **Conjecture:** a mathematically or physically motivated proposition not yet established.
- **Physical hypothesis:** a proposal about nature that requires empirical assessment.
- **Empirical support:** evidence from observation or experiment, assessed in relation to uncertainty and alternative explanations.

A mathematically consistent construction is not thereby physically realized. A numerical result is not automatically an analytical proof. A proposal is not a discovery merely because it is new to this repository.

## Core principles

### Respect the domain of established theories

A theory may be incomplete or have unresolved foundations while remaining highly successful in its tested domain. Any proposed successor or extension must recover established results where those results are known to hold.

### Require physical motivation

Changes to a theory should be motivated by a clearly stated problem, explanatory goal, or mathematically meaningful question—not by novelty alone.

### Make assumptions inspectable

State assumptions explicitly, including symmetry conditions, boundary conditions, coordinate choices, approximations, regularity requirements, and parameter restrictions when relevant.

### Treat consistency as a set of obligations

The relevant checks depend on the theory, but may include dimensional consistency, covariance, conservation laws, symmetries, limiting behaviour, stability, regularity, causality, and compatibility with established constraints.

### Report negative results

A derivation that reproduces a known result, rules out a proposed modification under stated assumptions, or exposes an inconsistency can be valuable. Conclusions must remain proportional to the analysis.

## Role of computation and formal methods

Analytical reasoning is central. Symbolic computation, numerical simulation, statistical analysis, and proof assistants may support derivations, explore examples, or check implementation details. They do not replace physical interpretation or the need to justify assumptions.

Computational and formal-methods experiments in the repository should state exactly what they establish and what they do not establish.

## Initial milestone

The first planned investigation is **AST-GR-001 — Schwarzschild Spacetime: Mathematical Foundations and Geodesic Structure**. Its first goal is to establish a reliable mathematical baseline from the Schwarzschild solution before considering any extension.

## Authorship and review

Research notes should identify their author, date, version, sources, and status. Claims should be open to correction. Uncertainty and unresolved issues should be recorded rather than concealed.
