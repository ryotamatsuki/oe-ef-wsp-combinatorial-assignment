import OEEFWSP.SixType

namespace OEEFWSP

/-- A lottery row over the full real-valued fractional feasible set. -/
structure RealRow where
  a : ℝ
  b : ℝ
  ab : ℝ
  empty : ℝ
  deriving Repr

namespace RealRow

/-- Probability assigned to a named bundle. -/
def prob (x : RealRow) : Bundle → ℝ
  | .a => x.a
  | .b => x.b
  | .ab => x.ab
  | .empty => x.empty

/-- Total probability mass in a row. -/
def mass (x : RealRow) : ℝ := x.a + x.b + x.ab + x.empty

/-- Componentwise nonnegativity. -/
def Nonnegative (x : RealRow) : Prop :=
  0 ≤ x.a ∧ 0 ≤ x.b ∧ 0 ≤ x.ab ∧ 0 ≤ x.empty

end RealRow

/-- A three-agent outcome over real-valued bundle probabilities. -/
structure RealOutcome where
  r0 : RealRow
  r1 : RealRow
  r2 : RealRow
  deriving Repr

namespace RealOutcome

/-- Total use of good a; bundle ab consumes one unit of a. -/
def goodAMass (x : RealOutcome) : ℝ :=
  x.r0.a + x.r1.a + x.r2.a + x.r0.ab + x.r1.ab + x.r2.ab

/-- Total use of good b; bundle ab consumes one unit of b. -/
def goodBMass (x : RealOutcome) : ℝ :=
  x.r0.b + x.r1.b + x.r2.b + x.r0.ab + x.r1.ab + x.r2.ab

end RealOutcome

/-- The original continuous fractional feasible set, with no denominator restriction. -/
def RealFeasible (x : RealOutcome) : Prop :=
  x.r0.Nonnegative ∧
  x.r1.Nonnegative ∧
  x.r2.Nonnegative ∧
  x.r0.mass = 1 ∧
  x.r1.mass = 1 ∧
  x.r2.mass = 1 ∧
  x.goodAMass ≤ 1 ∧
  x.goodBMass ≤ 1

/-- Embed an exact rational mechanism row into the continuous real domain. -/
def castRow (x : Row) : RealRow :=
  ⟨x.a, x.b, x.ab, x.empty⟩

/-- Embed an exact rational mechanism outcome into the continuous real domain. -/
def castOutcome (x : Outcome) : RealOutcome :=
  ⟨castRow x.r0, castRow x.r1, castRow x.r2⟩

/-- Top-one cumulative probability under a six-type strict ranking. -/
def realCum1 (t : SixType) (x : RealRow) : ℝ := x.prob (first t)

/-- Top-two cumulative probability under a six-type strict ranking. -/
def realCum2 (t : SixType) (x : RealRow) : ℝ :=
  x.prob (first t) + x.prob (second t)

/-- Top-three cumulative probability under a six-type strict ranking. -/
def realCum3 (t : SixType) (x : RealRow) : ℝ :=
  x.prob (first t) + x.prob (second t) + x.prob (third t)

/-- Bundle-level weak stochastic dominance on real-valued lotteries. -/
def RealSDWeak (t : SixType) (x y : RealRow) : Prop :=
  realCum1 t x ≥ realCum1 t y ∧
  realCum2 t x ≥ realCum2 t y ∧
  realCum3 t x ≥ realCum3 t y

/-- Strict SD improvement at at least one non-trivial cutoff. -/
def StrictAtSomeCutoff (t : SixType) (x y : RealRow) : Prop :=
  realCum1 t x > realCum1 t y ∨
  realCum2 t x > realCum2 t y ∨
  realCum3 t x > realCum3 t y

/--
A feasible real-valued outcome is an SD-Pareto improvement over the T1 mechanism
if every agent weakly SD-improves and at least one agent strictly improves at a cutoff.
-/
def SDParetoImprovesAt (t0 t1 t2 : SixType) (y : RealOutcome) : Prop :=
  let x := castOutcome (mechanism t0 t1 t2)
  RealSDWeak t0 y.r0 x.r0 ∧
  RealSDWeak t1 y.r1 x.r1 ∧
  RealSDWeak t2 y.r2 x.r2 ∧
  (StrictAtSomeCutoff t0 y.r0 x.r0 ∨
   StrictAtSomeCutoff t1 y.r1 x.r1 ∨
   StrictAtSomeCutoff t2 y.r2 x.r2)

/-- Ordinal efficiency against the unrestricted continuous fractional feasible set. -/
def ContinuousOrdinallyEfficientAt (t0 t1 t2 : SixType) : Prop :=
  ∀ y : RealOutcome, RealFeasible y → ¬ SDParetoImprovesAt t0 t1 t2 y

/--
T1 continuous OE theorem. The comparison outcome is arbitrary over ℝ; there is
no candidate-set, denominator, deterministic-decomposition, or vertex restriction.
-/
theorem sixType_continuous_ordinallyEfficient (t0 t1 t2 : SixType) :
    ContinuousOrdinallyEfficientAt t0 t1 t2 := by
  intro y hy himprove
  rcases hy with ⟨hy0, hy1, hy2, hm0, hm1, hm2, hcapA, hcapB⟩
  rcases hy0 with ⟨h0a, h0b, h0ab, h0e⟩
  rcases hy1 with ⟨h1a, h1b, h1ab, h1e⟩
  rcases hy2 with ⟨h2a, h2b, h2ab, h2e⟩
  rcases himprove with ⟨hw0, hw1, hw2, hs⟩
  rcases hw0 with ⟨hw01, hw02, hw03⟩
  rcases hw1 with ⟨hw11, hw12, hw13⟩
  rcases hw2 with ⟨hw21, hw22, hw23⟩
  rcases hs with hs0 | hs1 | hs2
  · rcases hs0 with hs01 | hs02 | hs03
    all_goals
      cases t0 <;> cases t1 <;> cases t2 <;>
        norm_num [RealRow.mass, RealOutcome.goodAMass, RealOutcome.goodBMass,
          realCum1, realCum2, realCum3, RealRow.prob,
          castOutcome, castRow, mechanism, leftCount, leftIndicator, isLeft,
          tableRow, first, second, third] at * <;>
        linarith
  · rcases hs1 with hs11 | hs12 | hs13
    all_goals
      cases t0 <;> cases t1 <;> cases t2 <;>
        norm_num [RealRow.mass, RealOutcome.goodAMass, RealOutcome.goodBMass,
          realCum1, realCum2, realCum3, RealRow.prob,
          castOutcome, castRow, mechanism, leftCount, leftIndicator, isLeft,
          tableRow, first, second, third] at * <;>
        linarith
  · rcases hs2 with hs21 | hs22 | hs23
    all_goals
      cases t0 <;> cases t1 <;> cases t2 <;>
        norm_num [RealRow.mass, RealOutcome.goodAMass, RealOutcome.goodBMass,
          realCum1, realCum2, realCum3, RealRow.prob,
          castOutcome, castRow, mechanism, leftCount, leftIndicator, isLeft,
          tableRow, first, second, third] at * <;>
        linarith

end OEEFWSP
