/-!
# Basic propositional reasoning

Small foundational lemmas used to demonstrate machine-checked reasoning
from explicitly stated premises.
-/

namespace AST

/-- Modus ponens: from P and P → Q, derive Q. -/
theorem modus_ponens {P Q : Prop} (hP : P) (hPQ : P → Q) : Q :=
  hPQ hP

/-- Conjunction introduction from two established propositions. -/
theorem conjunction_intro {P Q : Prop} (hP : P) (hQ : Q) : P ∧ Q :=
  And.intro hP hQ

end AST
