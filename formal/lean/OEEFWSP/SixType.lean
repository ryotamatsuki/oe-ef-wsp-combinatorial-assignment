import OEEFWSP.Basic

namespace OEEFWSP

/-- Canonical six-type domain D† = {A,B,E,F,C,D}. -/
inductive SixType where
  | A
  | B
  | E
  | F
  | C
  | D
  deriving DecidableEq, Repr

/-- Left/right classification used by the explicit mechanism. -/
def isLeft : SixType → Bool
  | .A | .E | .C => true
  | .B | .F | .D => false

/-- Numeric indicator for counting left reports. -/
def leftIndicator : SixType → Nat
  | .A | .E | .C => 1
  | .B | .F | .D => 0

/-- Number of left reports in a three-agent profile. -/
def leftCount (t0 t1 t2 : SixType) : Nat :=
  leftIndicator t0 + leftIndicator t1 + leftIndicator t2

/--
The exact rational row table from `src/mechanism_six_type.py`.
The fallback branch is unreachable when called by `mechanism`; it only makes the
function total on arbitrary natural numbers and impossible endpoint/group pairs.
-/
def tableRow : Nat → Bool → Row
  | 0, false => ⟨(1 : ℚ) / 3, (1 : ℚ) / 3, 0, (1 : ℚ) / 3⟩
  | 1, true  => ⟨(2 : ℚ) / 3, 0, 0, (1 : ℚ) / 3⟩
  | 1, false => ⟨(1 : ℚ) / 6, (1 : ℚ) / 2, 0, (1 : ℚ) / 3⟩
  | 2, true  => ⟨(1 : ℚ) / 2, (1 : ℚ) / 6, 0, (1 : ℚ) / 3⟩
  | 2, false => ⟨0, (2 : ℚ) / 3, 0, (1 : ℚ) / 3⟩
  | 3, true  => ⟨(1 : ℚ) / 3, (1 : ℚ) / 3, 0, (1 : ℚ) / 3⟩
  | _, _     => ⟨0, 0, 0, 1⟩

/-- Explicit six-type mechanism for a three-agent ordered profile. -/
def mechanism (t0 t1 t2 : SixType) : Outcome :=
  let k := leftCount t0 t1 t2
  ⟨tableRow k (isLeft t0), tableRow k (isLeft t1), tableRow k (isLeft t2)⟩

/-- First-ranked bundle. -/
def first : SixType → Bundle
  | .A => .a
  | .B => .b
  | .E => .a
  | .F => .b
  | .C => .ab
  | .D => .ab

/-- Second-ranked bundle. -/
def second : SixType → Bundle
  | .A => .b
  | .B => .a
  | .E => .ab
  | .F => .ab
  | .C => .a
  | .D => .b

/-- Third-ranked bundle. -/
def third : SixType → Bundle
  | .A => .empty
  | .B => .empty
  | .E => .b
  | .F => .a
  | .C => .b
  | .D => .a

/-- Top-one cumulative probability under the true strict ranking. -/
def cum1 (t : SixType) (x : Row) : ℚ := x.prob (first t)

/-- Top-two cumulative probability under the true strict ranking. -/
def cum2 (t : SixType) (x : Row) : ℚ :=
  x.prob (first t) + x.prob (second t)

/-- Top-three cumulative probability under the true strict ranking. -/
def cum3 (t : SixType) (x : Row) : ℚ :=
  x.prob (first t) + x.prob (second t) + x.prob (third t)

/--
Bundle-level weak stochastic dominance for a strict four-bundle ranking.
Only the three non-trivial cutoffs are required.
-/
def SDWeak (t : SixType) (x y : Row) : Prop :=
  cum1 t x ≥ cum1 t y ∧
  cum2 t x ≥ cum2 t y ∧
  cum3 t x ≥ cum3 t y

/-- Explicit decidability used by the exact finite SD checker. -/
instance sdWeakDecidable (t : SixType) (x y : Row) : Decidable (SDWeak t x y) := by
  unfold SDWeak
  infer_instance

/-- Exact envy-freeness at an ordered three-agent profile (self-comparisons omitted). -/
def EnvyFreeAt (t0 t1 t2 : SixType) : Prop :=
  let x := mechanism t0 t1 t2
  SDWeak t0 x.r0 x.r1 ∧
  SDWeak t0 x.r0 x.r2 ∧
  SDWeak t1 x.r1 x.r0 ∧
  SDWeak t1 x.r1 x.r2 ∧
  SDWeak t2 x.r2 x.r0 ∧
  SDWeak t2 x.r2 x.r1

instance envyFreeAtDecidable (t0 t1 t2 : SixType) : Decidable (EnvyFreeAt t0 t1 t2) := by
  unfold EnvyFreeAt
  infer_instance

/-- Truthful row for agent 0 weakly SD-dominates its row after a report change. -/
def TruthDominatesDeviation0 (t0 t1 t2 mis : SixType) : Prop :=
  SDWeak t0 (mechanism t0 t1 t2).r0 (mechanism mis t1 t2).r0

/-- Truthful row for agent 1 weakly SD-dominates its row after a report change. -/
def TruthDominatesDeviation1 (t0 t1 t2 mis : SixType) : Prop :=
  SDWeak t1 (mechanism t0 t1 t2).r1 (mechanism t0 mis t2).r1

/-- Truthful row for agent 2 weakly SD-dominates its row after a report change. -/
def TruthDominatesDeviation2 (t0 t1 t2 mis : SixType) : Prop :=
  SDWeak t2 (mechanism t0 t1 t2).r2 (mechanism t0 t1 mis).r2

instance truthDominatesDeviation0Decidable (t0 t1 t2 mis : SixType) :
    Decidable (TruthDominatesDeviation0 t0 t1 t2 mis) := by
  unfold TruthDominatesDeviation0
  infer_instance

instance truthDominatesDeviation1Decidable (t0 t1 t2 mis : SixType) :
    Decidable (TruthDominatesDeviation1 t0 t1 t2 mis) := by
  unfold TruthDominatesDeviation1
  infer_instance

instance truthDominatesDeviation2Decidable (t0 t1 t2 mis : SixType) :
    Decidable (TruthDominatesDeviation2 t0 t1 t2 mis) := by
  unfold TruthDominatesDeviation2
  infer_instance

/--
A single universally quantified report variable checks all three agent positions.
Since `mis` is arbitrary, this is full bundle-level SD-strategy-proofness.
-/
def FullSDStrategyProofAgainst (t0 t1 t2 mis : SixType) : Prop :=
  TruthDominatesDeviation0 t0 t1 t2 mis ∧
  TruthDominatesDeviation1 t0 t1 t2 mis ∧
  TruthDominatesDeviation2 t0 t1 t2 mis

instance fullSDStrategyProofAgainstDecidable (t0 t1 t2 mis : SixType) :
    Decidable (FullSDStrategyProofAgainst t0 t1 t2 mis) := by
  unfold FullSDStrategyProofAgainst
  infer_instance

/-- Every reachable table row is fractionally feasible at every one of the 216 ordered profiles. -/
theorem sixType_feasible (t0 t1 t2 : SixType) :
    Feasible (mechanism t0 t1 t2) := by
  cases t0 <;> cases t1 <;> cases t2 <;> native_decide

/-- All 3,888 non-self bundle-SD EF cutoff inequalities hold exactly. -/
theorem sixType_envyFree (t0 t1 t2 : SixType) :
    EnvyFreeAt t0 t1 t2 := by
  cases t0 <;> cases t1 <;> cases t2 <;> native_decide

/--
Full bundle-level SD-strategy-proofness on D†.
This includes truthful-to-truthful report comparisons; restricting to genuine
misreports yields the 3,240 unilateral deviations in the Python regression suite.
-/
theorem sixType_fullSDStrategyProof (t0 t1 t2 mis : SixType) :
    FullSDStrategyProofAgainst t0 t1 t2 mis := by
  cases t0 <;> cases t1 <;> cases t2 <;> cases mis <;> native_decide

end OEEFWSP
