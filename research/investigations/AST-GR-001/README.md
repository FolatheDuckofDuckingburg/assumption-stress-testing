# AST-GR-001 — Schwarzschild Spacetime

**Status:** Planned — foundations and baseline derivations  
**Research area:** General relativity / black-hole physics  
**Primary objective:** Derive and understand the geometry and geodesic structure of the Schwarzschild solution.

## Research question

How does the Schwarzschild spacetime geometry determine the motion of massive and massless test particles, and how do its geometric properties constrain stable and unstable orbital motion?

This is a foundational study of an established exact solution of general relativity. It is not initially a search for a new black-hole model.

## Scope

The investigation will focus on the vacuum Schwarzschild solution: a static, spherically symmetric spacetime outside a non-rotating, uncharged, isolated mass, under the assumptions appropriate to the solution.

Planned topics:

1. Derivation and interpretation of the Schwarzschild line element.
2. Coordinate conventions, units, and the meaning of the Schwarzschild radial coordinate.
3. Curvature quantities and invariant checks.
4. Killing symmetries and conserved quantities for geodesic motion.
5. Timelike geodesics and effective-potential analysis.
6. Circular timelike orbits and their stability.
7. Null geodesics, light deflection, and the photon sphere.
8. The innermost stable circular orbit (ISCO).
9. Limiting cases and comparison with the Newtonian regime.
10. Numerical checks of selected analytical results, if useful.

## Baseline equations and conventions

The study will explicitly state its metric signature and unit convention. A standard starting convention is geometrized units (G=c=1) and signature ((-+++)), with Schwarzschild line element

[
ds^2 = -\left(1-\frac{2M}{r}\right)dt^2
+\left(1-\frac{2M}{r}\right)^{-1}dr^2
+r^2(d\theta^2+\sin^2\theta\,d\phi^2).
]

The coordinate expression is a starting point, not a complete physical interpretation. Coordinate singularities, curvature invariants, and the spacetime's causal structure must be treated carefully.

## Planned derivations

The work should derive, rather than merely quote, the following where feasible:

- The metric from the assumptions defining the Schwarzschild solution, or a clearly cited derivation if the full derivation is outside the initial scope.
- Relevant Christoffel symbols and curvature quantities.
- Geodesic equations and conserved energy/angular momentum associated with symmetries.
- Effective potentials for timelike and null geodesics.
- Conditions for circular orbits and their stability.
- The photon-sphere and ISCO radii.

Known benchmark values, such as the photon-sphere radius (r=3M) and the ISCO radius (r=6M) for the standard Schwarzschild solution, are targets for independent derivation and verification—not results to assume without checking.

## Validation and consistency checks

The investigation should include:

- Dimensional consistency when restoring (G) and (c).
- Signature and sign-convention checks.
- Verification of the vacuum field equations in the region where the solution applies.
- Curvature-invariant checks to distinguish coordinate singularities from curvature singularities.
- Weak-field / large-radius behaviour.
- Consistency of conserved quantities and geodesic normalization.
- Comparison of analytical results with an independently implemented numerical calculation, where appropriate.

Numerical agreement is a verification aid and must not be presented as a proof of the underlying theory.

## Deliverables

The intended outputs are:

- A versioned derivation notebook or manuscript.
- A notation and conventions sheet.
- Reproducible symbolic or numerical checks, if used.
- A bibliography of primary and authoritative sources.
- A record of discrepancies, corrections, and open questions.

## Boundaries

This study does not, by itself:

- Test quantum gravity.
- Describe rotating or charged black holes.
- Establish new physics.
- Demonstrate that general relativity is incomplete or incorrect.
- Establish observational claims about a specific astrophysical black hole.

Extensions to Kerr geometry, perturbations, semiclassical effects, or alternative models should be separate studies with their own questions and assumptions.

## Research log

No derivations or results are claimed in this brief. Work should be added with dates, references, explicit calculations, and a clear status label.
