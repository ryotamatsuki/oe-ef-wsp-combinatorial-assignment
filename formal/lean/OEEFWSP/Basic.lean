import Mathlib

namespace OEEFWSP

/-- The four bundles in the two-good assignment model. -/
inductive Bundle where
  | a
  | b
  | ab
  | empty
  deriving DecidableEq, Repr

/-- An exact rational lottery over bundles. -/
structure Row where
  a : ℚ
  b : ℚ
  ab : ℚ
  empty : ℚ
  deriving DecidableEq, Repr

namespace Row

/-- Probability assigned to a named bundle. -/
def prob (x : Row) : Bundle → ℚ
  | .a => x.a
  | .b => x.b
  | .ab => x.ab
  | .empty => x.empty

/-- Total probability mass in a row. -/
def mass (x : Row) : ℚ := x.a + x.b + x.ab + x.empty

/-- Componentwise nonnegativity. -/
def Nonnegative (x : Row) : Prop :=
  0 ≤ x.a ∧ 0 ≤ x.b ∧ 0 ≤ x.ab ∧ 0 ≤ x.empty

end Row

/-- A three-agent fractional outcome. -/
structure Outcome where
  r0 : Row
  r1 : Row
  r2 : Row
  deriving DecidableEq, Repr

namespace Outcome

/-- Total use of good a; bundle ab consumes one unit of a. -/
def goodAMass (x : Outcome) : ℚ :=
  x.r0.a + x.r1.a + x.r2.a + x.r0.ab + x.r1.ab + x.r2.ab

/-- Total use of good b; bundle ab consumes one unit of b. -/
def goodBMass (x : Outcome) : ℚ :=
  x.r0.b + x.r1.b + x.r2.b + x.r0.ab + x.r1.ab + x.r2.ab

end Outcome

/-- Fractional feasibility for three agents and two unit-supply goods. -/
def Feasible (x : Outcome) : Prop :=
  x.r0.Nonnegative ∧
  x.r1.Nonnegative ∧
  x.r2.Nonnegative ∧
  x.r0.mass = 1 ∧
  x.r1.mass = 1 ∧
  x.r2.mass = 1 ∧
  x.goodAMass ≤ 1 ∧
  x.goodBMass ≤ 1

/-- Explicit decidability used by the exact finite checker. -/
instance feasibleDecidable (x : Outcome) : Decidable (Feasible x) := by
  unfold Feasible Row.Nonnegative
  infer_instance

end OEEFWSP
