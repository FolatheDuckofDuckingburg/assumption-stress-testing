/-!
# Refutation vocabulary

This module introduces a minimal logical vocabulary for expressing that a
proposition is refuted. It does not yet implement an automated
counterexample-search procedure.
-/

namespace AST

/-- A proposition is refuted when its negation is established. -/
def Refutes (Γ : List Prop) (P : Prop) : Prop :=
  (∀ Q, Q ∈ Γ → Q) → ¬ P

/-- A counterexample to a proposition, at this logical level, is a proof of its negation. -/
def Counterexample (P : Prop) : Prop :=
  ¬ P

/-- A refutation from a context yields a counterexample when the context holds. -/
theorem refutation_yields_counterexample {Γ : List Prop} {P : Prop}
    (hRefutes : Refutes Γ P)
    (hΓ : ∀ Q, Q ∈ Γ → Q) : Counterexample P :=
  hRefutes hΓ

end AST
