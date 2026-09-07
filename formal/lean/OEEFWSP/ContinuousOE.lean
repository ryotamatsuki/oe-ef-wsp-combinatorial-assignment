import OEEFWSP.SixType

namespace OEEFWSP

/-- A lottery row over the full real-valued fractional feasible set. -/
structure RealRow where
  a : ℝ
  b : ℝ
  ab : ℝ
  empty : ℝ

namespace RealRow

/-- Probability assigned to a named bundle. -/
def prob (x : RealRow) : Bundle → ℝ
  | .a => x.a
  | .b => x.b
  | .ab => x.ab
  | .empty => x.empty

/-- Total probability mass in a row. -/
def mass (x : RealRow) : ℝ := x.a + x.b + x.ab + x.empty

/-- Total probability of receiving a nonempty bundle. -/
def nonemptyMass (x : RealRow) : ℝ := x.a + x.b + x.ab

/-- Componentwise nonnegativity. -/
def Nonnegative (x : RealRow) : Prop :=
  0 ≤ x.a ∧ 0 ≤ x.b ∧ 0 ≤ x.ab ∧ 0 ≤ x.empty

end RealRow

/-- A three-agent outcome over real-valued bundle probabilities. -/
structure RealOutcome where
  r0 : RealRow
  r1 : RealRow
  r2 : RealRow

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

/-- Turn the L/R side bit into the same natural indicator used by the mechanism. -/
def sideIndicator : Bool → Nat
  | false => 0
  | true => 1

/-- Number of L-side reports, expressed only in terms of the three side bits. -/
def sideCount (l0 l1 l2 : Bool) : Nat :=
  sideIndicator l0 + sideIndicator l1 + sideIndicator l2

/-- The six-type benchmark depends only on the three L/R side bits. -/
def sideBenchmark (l0 l1 l2 : Bool) : RealOutcome :=
  let k := sideCount l0 l1 l2
  ⟨castRow (tableRow k l0), castRow (tableRow k l1), castRow (tableRow k l2)⟩

/-- The type-level left indicator is exactly the side-bit indicator. -/
theorem leftIndicator_eq_sideIndicator (t : SixType) :
    leftIndicator t = sideIndicator (isLeft t) := by
  cases t <;> rfl

/-- Casting the canonical mechanism to ℝ gives the side-bit benchmark. -/
theorem castOutcome_mechanism_eq_sideBenchmark (t0 t1 t2 : SixType) :
    castOutcome (mechanism t0 t1 t2) =
      sideBenchmark (isLeft t0) (isLeft t1) (isLeft t2) := by
  unfold mechanism leftCount sideBenchmark sideCount
  rw [leftIndicator_eq_sideIndicator t0,
      leftIndicator_eq_sideIndicator t1,
      leftIndicator_eq_sideIndicator t2]

/-- Every reachable benchmark row has zero `ab` mass and singleton mass 2/3. -/
theorem sideBenchmark_row_shape (l0 l1 l2 : Bool) :
    let x := sideBenchmark l0 l1 l2
    x.r0.ab = 0 ∧ x.r0.a + x.r0.b = (2 : ℝ) / 3 ∧
    x.r1.ab = 0 ∧ x.r1.a + x.r1.b = (2 : ℝ) / 3 ∧
    x.r2.ab = 0 ∧ x.r2.a + x.r2.b = (2 : ℝ) / 3 := by
  cases l0 <;> cases l1 <;> cases l2 <;>
    norm_num [sideBenchmark, sideCount, sideIndicator, castRow, tableRow]

/--
Weak SD dominance over a benchmark row with zero pair mass and singleton mass 2/3
forces at least 2/3 probability on nonempty bundles. This is the common first
step in the analytic OE proof.
-/
theorem realSD_nonemptyMass_ge_twoThirds
    (t : SixType) (y x : RealRow)
    (hyab : 0 ≤ y.ab)
    (hxab : x.ab = 0)
    (hxsing : x.a + x.b = (2 : ℝ) / 3)
    (hSD : RealSDWeak t y x) :
    (2 : ℝ) / 3 ≤ y.nonemptyMass := by
  rcases hSD with ⟨h1, h2, h3⟩
  cases t <;>
    norm_num [realCum1, realCum2, realCum3, RealRow.prob,
      RealRow.nonemptyMass, first, second, third] at h1 h2 h3 ⊢ <;>
    linarith

/-- Preferred singleton coordinate, conditional only on the L/R side. -/
def preferredSingleton (left : Bool) (x : RealRow) : ℝ :=
  if left then x.a else x.b

/--
Once pair mass is zero on both rows, weak SD dominance implies that the agent's
preferred-singleton probability is weakly higher than at the benchmark.
-/
theorem realSD_preferredSingleton_ge
    (t : SixType) (y x : RealRow)
    (hyab : y.ab = 0)
    (hxab : x.ab = 0)
    (hSD : RealSDWeak t y x) :
    preferredSingleton (isLeft t) x ≤ preferredSingleton (isLeft t) y := by
  rcases hSD with ⟨h1, h2, h3⟩
  cases t <;>
    norm_num [preferredSingleton, realCum1, realCum2, realCum3,
      RealRow.prob, first, second, third] at h1 h2 h3 ⊢ <;>
    linarith

/--
For each of the eight possible L/R side profiles, feasibility together with fixed
2/3 singleton mass and the three preferred-singleton lower bounds pins down the
benchmark allocation uniquely. Only the finite side pattern is enumerated; the
comparison allocation remains arbitrary over ℝ.
-/
theorem sideBenchmark_unique_from_preferred
    (l0 l1 l2 : Bool) (y : RealOutcome)
    (hm0 : y.r0.mass = 1) (hm1 : y.r1.mass = 1) (hm2 : y.r2.mass = 1)
    (hy0ab : y.r0.ab = 0) (hy1ab : y.r1.ab = 0) (hy2ab : y.r2.ab = 0)
    (hn0 : y.r0.nonemptyMass = (2 : ℝ) / 3)
    (hn1 : y.r1.nonemptyMass = (2 : ℝ) / 3)
    (hn2 : y.r2.nonemptyMass = (2 : ℝ) / 3)
    (hcapA : y.goodAMass ≤ 1) (hcapB : y.goodBMass ≤ 1)
    (hp0 : preferredSingleton l0 (sideBenchmark l0 l1 l2).r0 ≤
      preferredSingleton l0 y.r0)
    (hp1 : preferredSingleton l1 (sideBenchmark l0 l1 l2).r1 ≤
      preferredSingleton l1 y.r1)
    (hp2 : preferredSingleton l2 (sideBenchmark l0 l1 l2).r2 ≤
      preferredSingleton l2 y.r2) :
    y = sideBenchmark l0 l1 l2 := by
  cases l0 <;> cases l1 <;> cases l2 <;>
    ext <;>
    norm_num [RealRow.mass, RealRow.nonemptyMass,
      RealOutcome.goodAMass, RealOutcome.goodBMass,
      preferredSingleton, sideBenchmark, sideCount, sideIndicator,
      castRow, tableRow] at * <;>
    linarith

/--
A stronger T1 statement: any continuously feasible allocation weakly SD-dominating
the mechanism must equal the mechanism. This directly mirrors the analytic proof.
-/
theorem sixType_continuous_weakSD_unique
    (t0 t1 t2 : SixType) (y : RealOutcome)
    (hy : RealFeasible y)
    (hSD0 : RealSDWeak t0 y.r0 (castOutcome (mechanism t0 t1 t2)).r0)
    (hSD1 : RealSDWeak t1 y.r1 (castOutcome (mechanism t0 t1 t2)).r1)
    (hSD2 : RealSDWeak t2 y.r2 (castOutcome (mechanism t0 t1 t2)).r2) :
    y = castOutcome (mechanism t0 t1 t2) := by
  let l0 := isLeft t0
  let l1 := isLeft t1
  let l2 := isLeft t2
  let x := sideBenchmark l0 l1 l2
  have hcast : castOutcome (mechanism t0 t1 t2) = x := by
    simpa [l0, l1, l2, x] using castOutcome_mechanism_eq_sideBenchmark t0 t1 t2
  rw [hcast] at hSD0 hSD1 hSD2
  rcases sideBenchmark_row_shape l0 l1 l2 with
    ⟨hx0ab, hx0sing, hx1ab, hx1sing, hx2ab, hx2sing⟩
  rcases hy with ⟨hy0, hy1, hy2, hm0, hm1, hm2, hcapA, hcapB⟩
  rcases hy0 with ⟨h0a, h0b, h0ab, h0e⟩
  rcases hy1 with ⟨h1a, h1b, h1ab, h1e⟩
  rcases hy2 with ⟨h2a, h2b, h2ab, h2e⟩
  have hn0ge : (2 : ℝ) / 3 ≤ y.r0.nonemptyMass :=
    realSD_nonemptyMass_ge_twoThirds t0 y.r0 x.r0 h0ab hx0ab hx0sing hSD0
  have hn1ge : (2 : ℝ) / 3 ≤ y.r1.nonemptyMass :=
    realSD_nonemptyMass_ge_twoThirds t1 y.r1 x.r1 h1ab hx1ab hx1sing hSD1
  have hn2ge : (2 : ℝ) / 3 ≤ y.r2.nonemptyMass :=
    realSD_nonemptyMass_ge_twoThirds t2 y.r2 x.r2 h2ab hx2ab hx2sing hSD2
  have habSumLe : y.r0.ab + y.r1.ab + y.r2.ab ≤ 0 := by
    dsimp [RealOutcome.goodAMass, RealOutcome.goodBMass,
      RealRow.nonemptyMass] at hcapA hcapB hn0ge hn1ge hn2ge ⊢
    linarith
  have hy0ab : y.r0.ab = 0 := by linarith
  have hy1ab : y.r1.ab = 0 := by linarith
  have hy2ab : y.r2.ab = 0 := by linarith
  have hn0 : y.r0.nonemptyMass = (2 : ℝ) / 3 := by
    dsimp [RealOutcome.goodAMass, RealOutcome.goodBMass,
      RealRow.nonemptyMass] at hcapA hcapB hn0ge hn1ge hn2ge ⊢
    linarith
  have hn1 : y.r1.nonemptyMass = (2 : ℝ) / 3 := by
    dsimp [RealOutcome.goodAMass, RealOutcome.goodBMass,
      RealRow.nonemptyMass] at hcapA hcapB hn0ge hn1ge hn2ge ⊢
    linarith
  have hn2 : y.r2.nonemptyMass = (2 : ℝ) / 3 := by
    dsimp [RealOutcome.goodAMass, RealOutcome.goodBMass,
      RealRow.nonemptyMass] at hcapA hcapB hn0ge hn1ge hn2ge ⊢
    linarith
  have hp0 : preferredSingleton l0 x.r0 ≤ preferredSingleton l0 y.r0 := by
    simpa [l0] using realSD_preferredSingleton_ge t0 y.r0 x.r0 hy0ab hx0ab hSD0
  have hp1 : preferredSingleton l1 x.r1 ≤ preferredSingleton l1 y.r1 := by
    simpa [l1] using realSD_preferredSingleton_ge t1 y.r1 x.r1 hy1ab hx1ab hSD1
  have hp2 : preferredSingleton l2 x.r2 ≤ preferredSingleton l2 y.r2 := by
    simpa [l2] using realSD_preferredSingleton_ge t2 y.r2 x.r2 hy2ab hx2ab hSD2
  have hyx : y = x := by
    simpa [x] using sideBenchmark_unique_from_preferred l0 l1 l2 y
      hm0 hm1 hm2 hy0ab hy1ab hy2ab hn0 hn1 hn2 hcapA hcapB hp0 hp1 hp2
  exact hyx.trans hcast.symm

/--
T1 continuous OE theorem. The comparison outcome is arbitrary over ℝ; there is
no candidate-set, denominator, deterministic-decomposition, or vertex restriction.
-/
theorem sixType_continuous_ordinallyEfficient (t0 t1 t2 : SixType) :
    ContinuousOrdinallyEfficientAt t0 t1 t2 := by
  intro y hy himprove
  rcases himprove with ⟨hSD0, hSD1, hSD2, hstrict⟩
  have hyx := sixType_continuous_weakSD_unique t0 t1 t2 y hy hSD0 hSD1 hSD2
  rw [hyx] at hstrict
  simp [StrictAtSomeCutoff] at hstrict

end OEEFWSP
