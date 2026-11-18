# AST Formalization

## Purpose

The Lean 4 module provides a small formal environment for expressing
assumption contexts and checking elementary logical consequences. It is a
formal-methods component of Assumption Stress Testing (AST), separate from
the Python synthetic graph-recovery benchmark.

## Current scope

The initial milestone includes:

- A finite context of propositions (AST.Context).
- A context-entailment relation (AST.Entails).
- A weakening theorem showing that adding assumptions preserves an existing
  entailment.
- Basic propositional reasoning examples.
- A minimal vocabulary for refutation and counterexamples.

These definitions are intentionally modest. They demonstrate how assumptions
and deductions can be represented in Lean; they do not constitute a general
theory-analysis engine or an automated counterexample generator.

## Build

Install Lean 4 using the instructions at https://lean-lang.org/install/.

From the repository root:

    cd formal/lean
    lake build

The Lean version is pinned in lean-toolchain.

## Interpretation and limitations

Lean checks that a proof follows from its formal definitions and premises
within Lean's logical foundation. It does not determine whether those premises
are physically true, whether a mathematical model describes nature, or whether
a theory agrees with experiment.

A machine-checked proof is therefore evidence of formal derivability, not
empirical confirmation.

Future work may formalize carefully selected mathematical claims from
computational or theoretical models. Any such formalization should document
the correspondence between the Lean definitions and the intended mathematics.
