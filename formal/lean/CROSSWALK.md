# Formalization crosswalk

This file prevents a green Lean build from being mistaken for a proof of a differently stated manuscript theorem.

| Canonical source | Mathematical object / claim | Lean declaration | Status |
|---|---|---|---|
| `src/preferences.py` | Bundles `(a,b,ab,empty)` | `OEEFWSP.Bundle` | FORMALIZED |
| `src/preferences.py` | Six strict rankings `A,B,E,F,C,D` | `OEEFWSP.SixType`, `first`, `second`, `third` | FORMALIZED |
| `src/preferences.py` | Bundle-level SD cumulative cutoffs | `cum1`, `cum2`, `cum3`, `SDWeak` | FORMALIZED |
| `src/mechanism_six_type.py` | L/R classification and `k` | `isLeft`, `leftIndicator`, `leftCount` | FORMALIZED |
| `src/mechanism_six_type.py` | Exact six-type allocation table | `tableRow`, `mechanism` | FORMALIZED |
| `theory/six_type_explicit_mechanism.md` | Fractional feasibility | `sixType_feasible` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Envy-freeness under bundle-level SD | `sixType_envyFree` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Full bundle-level SD-strategy-proofness | `sixType_fullSDStrategyProof` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Ordinal efficiency against the full continuous fractional feasible set | `sixType_continuous_ordinallyEfficient` | LEAN-CERTIFIED |
| `docs/THEOREM_STATUS.md` T1 | Combined OE+EF+full SD-SP existence theorem | `sixType_feasible`, `sixType_envyFree`, `sixType_fullSDStrategyProof`, `sixType_continuous_ordinallyEfficient` | FULLY LEAN-CERTIFIED |

## Exact counting correspondence

For each of the `6^3 = 216` ordered profiles:

- EF checks 3 agents × 2 other agents × 3 non-trivial SD cutoffs, giving `216 × 18 = 3,888` exact cutoff inequalities.
- Full SD-SP checks 3 agent positions × 6 possible reports. The Lean theorem includes the truthful report as a weak-dominance equality case. Removing the truthful report leaves `216 × 3 × 5 = 3,240` genuine unilateral deviations, matching the canonical Python count.

## Continuous OE scope

The Lean theorem `sixType_continuous_ordinallyEfficient` quantifies over arbitrary real-valued comparison outcomes in the original continuous fractional feasible set. The formalization introduces no denominator restriction, candidate-set restriction, vertex restriction, or deterministic-decomposition restriction.

The comparison allocation is modeled over `ℝ`, bundle-level SD Pareto improvement is represented directly, and the substantive OE proof is accepted by Lean without `sorry` or an added axiom placeholder.

## T1 certification status

T1 is fully Lean-certified for the canonical six-type domain. The machine-checked layer covers fractional feasibility, bundle-level EF, full bundle-level SD-strategy-proofness, and ordinal efficiency against the unrestricted continuous fractional feasible set.
