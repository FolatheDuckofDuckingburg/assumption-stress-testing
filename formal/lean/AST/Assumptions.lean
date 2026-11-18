/-!
# Assumption contexts and entailment

This module provides a minimal logical representation of a context of
propositions and the relation of entailment used by the AST formalization.
It makes no claims about the physical truth of any proposition.
-/

namespace AST

/-- A context is a finite list of propositions treated as assumptions. -/
abbrev Context := List Prop

/-- A context entails P when P follows whenever every context assumption holds. -/
def Entails (Γ : Context) (P : Prop) : Prop :=
  (∀ Q, Q ∈ Γ → Q) → P

/-- A proposition follows from a context if it is already available as an assumption. -/
theorem assumption_is_entailed {Γ : Context} {P : Prop}
    (hP : P) : Entails (P :: Γ) P := by
  intro _
  exact hP

/-- Adding assumptions cannot invalidate an existing entailment. -/
theorem weakening {Γ Δ : Context} {P : Prop}
    (hSub : ∀ Q, Q ∈ Γ → Q ∈ Δ)
    (hEntails : Entails Γ P) : Entails Δ P := by
  intro hΔ
  apply hEntails
  intro Q hQ
  exact hΔ Q (hSub Q hQ)

/-- A consequence of an entailed proposition is also entailed. -/
theorem consequence_of_assumptions {Γ : Context} {P Q : Prop}
    (hP : Entails Γ P) (hPQ : P → Q) : Entails Γ Q := by
  intro hΓ
  exact hPQ (hP hΓ)

end AST
