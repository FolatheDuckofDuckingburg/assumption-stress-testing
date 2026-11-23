# AST-GR-001 — Schwarzschild Spacetime: Mathematical Foundations and Geodesic Structure

**Status:** Planned foundational study  
**Research area:** General relativity / black-hole physics  
**Primary objective:** Derive and reproduce established properties of the Schwarzschild solution.

## 1. Research question

How does the geometry of the Schwarzschild spacetime determine the motion of freely falling massive particles and light, and how do its characteristic radii arise from the metric and geodesic equations?

This study is deliberately focused on a known solution. Its first purpose is to establish mathematical competence and a checked baseline before AST attempts any generalization.

## 2. Scope

The Schwarzschild solution describes the vacuum exterior spacetime of a spherically symmetric, non-rotating, uncharged gravitating body. In the black-hole interpretation, the relevant mass parameter is (M).

The study will cover:

1. The Schwarzschild metric and coordinate conventions
2. Metric properties and coordinate singularities
3. Curvature tensors and curvature invariants
4. Timelike geodesics
5. Null geodesics
6. Circular timelike orbits and their stability
7. The photon sphere
8. The innermost stable circular orbit (ISCO)
9. Appropriate weak-field and Newtonian limits

The study will not initially cover rotating black holes, charged black holes, quantum effects, or speculative modifications of general relativity.

## 3. Conventions and starting point

Use metric signature ((- + + +)), Schwarzschild coordinates ((t,r,\theta,\phi)), and initially geometric units (G=c=1). The line element is

\[
 ds^2 = -\left(1-\frac{2M}{r}\right)dt^2
 + \left(1-\frac{2M}{r}\right)^{-1}dr^2
 + r^2 d\theta^2
 + r^2\sin^2\theta\,d\phi^2.
\]

When restoring SI units, replace the characteristic length (2M) by (2GM/c^2). Units and conventions must be stated consistently throughout all derivations.

The coordinate expression is singular at (r=2M), but this alone does not establish a curvature singularity. The study must distinguish coordinate singularities from invariant curvature singularities and explain the coordinate domain being used.

## 4. Derivation programme

### 4.1 Metric and curvature

- State the vacuum Einstein field equations used for the exterior solution.
- Identify the nonzero metric components and inverse metric.
- Derive or independently verify the relevant Christoffel symbols.
- Calculate the Riemann and Ricci tensors, or provide a transparent symbolic derivation checked independently.
- Verify that the exterior is Ricci-flat.
- Compute the Kretschmann scalar and interpret its radial dependence.

### 4.2 Geodesic equations

Start from the geodesic equation or the equivalent variational formulation. Use spherical symmetry to restrict motion to an orbital plane where appropriate. Identify conserved quantities associated with the spacetime's time-translation and rotational symmetries.

Derive the radial equation for timelike and null geodesics. Clearly distinguish proper time, affine parameter, and coordinate time.

### 4.3 Circular orbits and stability

Derive the conditions for circular timelike geodesics and analyze radial stability. Recover the established Schwarzschild ISCO result:

\[
r_{\mathrm{ISCO}} = 6M = \frac{6GM}{c^2}.
\]

The derivation must show how the circular-orbit and stability conditions produce this radius; quoting the result is not sufficient.

### 4.4 Photon sphere

Derive the condition for circular null geodesics and recover:

\[
r_{\mathrm{ph}} = 3M = \frac{3GM}{c^2}.
\]

Explain the distinction between the photon sphere and the event horizon.

### 4.5 Horizon and curvature singularity

For the Schwarzschild coordinate chart, identify the horizon radius:

\[
r_s = 2M = \frac{2GM}{c^2}.
\]

Use curvature invariants and, where useful, a horizon-regular coordinate system to distinguish the coordinate behaviour at the horizon from the physical curvature singularity at (r=0).

### 4.6 Weak-field limit

Show how the metric approaches the weak-field, slow-motion regime and identify the Newtonian gravitational potential. State the approximation conditions and explain which geodesic results reduce to Newtonian expectations.

## 5. Validation checklist

The study is not complete until the following have been checked:

- Metric signature and units are consistent.
- The inverse metric satisfies (g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu_\nu).
- The vacuum exterior satisfies (R_{\mu\nu}=0).
- Curvature invariants are coordinate-independent and have the expected dimensions.
- Conserved quantities follow from the relevant symmetries.
- Timelike and null radial equations are derived separately.
- Circular-orbit conditions and stability conditions are not conflated.
- The photon-sphere and ISCO radii are derived, not merely inserted.
- The weak-field limit agrees with the Newtonian regime.
- Any symbolic or numerical computation is checked against analytical results.

## 6. Expected deliverables

1. A self-contained derivation notebook or manuscript.
2. A notation and conventions sheet.
3. A verified set of key equations and intermediate steps.
4. Optional numerical visualizations of effective potentials or representative geodesics, with methods documented.
5. A bibliography of authoritative textbooks and relevant primary literature.
6. A short report separating reproduced results, implementation checks, and unresolved questions.

## 7. What would count as success

Success means producing a clear, internally consistent, independently checked account of the specified Schwarzschild results. Reproducing established results is a foundational milestone, not a novel discovery.

Any later extension must have a separate research question, motivation, mathematical definition, consistency analysis, and comparison with the existing literature. No physical novelty or empirical validity is claimed by this study specification.

## 8. Open questions for the study

- Which derivation route gives the clearest and most independently checkable presentation of the curvature tensors?
- Which symbolic computation tools, if any, will be used, and how will their output be validated?
- Which references will serve as the primary baseline for sign conventions and derivations?
- What numerical checks are genuinely useful beyond the analytical derivation?
