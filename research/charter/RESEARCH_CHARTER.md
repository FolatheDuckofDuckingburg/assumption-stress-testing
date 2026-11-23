# AST Research Charter

## 1. Identity

AST is an independent theoretical physics research initiative. AST is the project name and is not expanded as an acronym.

AST investigates physical theories through mathematical formulation, theoretical derivation, model development, and physical analysis. Its purpose is to conduct careful, bounded investigations rather than to make broad claims unsupported by derivation or evidence.

## 2. Scope

AST has a broad theoretical-physics remit. Areas may include:

- General relativity and gravitation
- Black-hole physics
- Quantum gravity
- Cosmology
- Quantum field theory
- Particle physics
- String theory and related frameworks
- Mathematical physics

A topic's inclusion in this charter indicates an area of interest, not that AST has completed research or established expertise in it. Each project must define its own scope and prerequisites.

## 3. What counts as a research contribution

Depending on the question, a contribution may take the form of:

- A careful derivation or independent reproduction of a known result
- A proof, proposition, counterexample, or mathematical classification
- An analytical solution or approximation
- A stability, perturbation, or limiting-case analysis
- A mathematically defined candidate model
- A derived physical prediction or constraint
- A computational method that enables or checks theoretical analysis
- A negative result that rules out or constrains a proposed approach

A new equation is not automatically a new physical theory. A mathematically consistent construction is not automatically physically realized.

## 4. Research workflow

A study should, where appropriate:

1. Formulate a precise physical question.
2. Identify the relevant theory, assumptions, conventions, and domain of validity.
3. Review prior work and define what is already known.
4. Reproduce key established results before making extensions.
5. Develop analytical derivations with explicit intermediate steps.
6. Use symbolic and numerical computation as supporting tools, with validation checks.
7. Examine consistency, symmetries, conservation laws, boundary conditions, limiting cases, and stability as relevant.
8. Interpret the mathematical result physically.
9. Identify empirical implications or explain why a claim is presently mathematical rather than empirically testable.
10. Document limitations, uncertainties, and unresolved questions.

The workflow is a guide, not a substitute for discipline-specific methods.

## 5. Standards

### Mathematical precision
Define notation, units, sign conventions, coordinate systems, assumptions, and domains. Distinguish exact statements from approximations.

### Literature engagement
Locate the relevant prior work. Do not describe a result as new until it has been compared with existing literature.

### Correspondence with established physics
Extensions of successful theories should recover their verified predictions in the appropriate regimes, or clearly explain which regime is being investigated and why the correspondence question differs.

### Physical accountability
Separate mathematical consistency, physical interpretation, and empirical support. Do not claim observational confirmation without appropriate evidence.

### Reproducibility
Keep derivations, references, source code, parameters, numerical methods, and validation procedures under version control where practical.

### Honest reporting
Report failed approaches, null results, and corrections. Do not manufacture precision, novelty, or experimental support.

## 6. Computation

Computation may support theoretical work through symbolic manipulation, numerical integration, simulation, parameter exploration, visualization, and independent checks. Computational output must be accompanied by method descriptions and validation.

A simulation is not a derivation. A numerical result is not automatically a physical prediction. Code should be tested against analytical limits, known solutions, convergence checks, or independent implementations where appropriate.

## 7. Research records

Each substantial study should maintain:

- A stable study identifier
- A concise research question
- A literature and background section
- Definitions, assumptions, and conventions
- Derivations and intermediate results
- Computational methods, if used
- Validation and consistency checks
- Results separated from interpretation
- Limitations and open questions
- References and reproducibility information

## 8. Initial programme

The first study, **AST-GR-001**, concerns the Schwarzschild solution and geodesic structure. It begins by reproducing established results in general relativity. It does not presume a modification to Einstein's theory.

## 9. Revision

This charter may evolve as AST develops. Changes should clarify scope and improve research standards without retroactively overstating what earlier work established.
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
