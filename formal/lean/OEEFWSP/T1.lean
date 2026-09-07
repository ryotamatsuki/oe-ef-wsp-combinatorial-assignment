import OEEFWSP.ContinuousOE

namespace OEEFWSP

/--
The paper-level T1 claim at a fixed ordered six-type profile: the explicit
mechanism is fractionally feasible, bundle-level envy-free, fully bundle-level
SD-strategy-proof against every six-type misreport, and ordinally efficient
against the unrestricted continuous real-valued fractional feasible set.

This declaration is the formalization-gap-audited paper-level conjunction used
for the T1 formal freeze.
-/
def T1At (t0 t1 t2 : SixType) : Prop :=
  Feasible (mechanism t0 t1 t2) ∧
  EnvyFreeAt t0 t1 t2 ∧
  (∀ mis : SixType, FullSDStrategyProofAgainst t0 t1 t2 mis) ∧
  ContinuousOrdinallyEfficientAt t0 t1 t2

/--
Combined T1 theorem, matching the canonical paper-level statement on D†.
-/
theorem sixType_T1 (t0 t1 t2 : SixType) : T1At t0 t1 t2 := by
  refine ⟨sixType_feasible t0 t1 t2, sixType_envyFree t0 t1 t2, ?_,
    sixType_continuous_ordinallyEfficient t0 t1 t2⟩
  intro mis
  exact sixType_fullSDStrategyProof t0 t1 t2 mis

end OEEFWSP
