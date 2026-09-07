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
| `theory/six_type_explicit_mechanism.md` | Ordinal efficiency against the full continuous fractional feasible set | — | NOT YET LEAN-CERTIFIED |
| `docs/THEOREM_STATUS.md` T1 | Combined OE+EF+full SD-SP existence theorem | — | PARTIALLY LEAN-CERTIFIED; OE REMAINS ANALYTIC |

## Exact counting correspondence

For each of the `6^3 = 216` ordered profiles:

- EF checks 3 agents × 2 other agents × 3 non-trivial SD cutoffs, giving `216 × 18 = 3,888` exact cutoff inequalities.
- Full SD-SP checks 3 agent positions × 6 possible reports. The Lean theorem includes the truthful report as a weak-dominance equality case. Removing the truthful report leaves `216 × 3 × 5 = 3,240` genuine unilateral deviations, matching the canonical Python count.

## Required audit before upgrading theorem status

Do not mark T1 as fully Lean-certified until all of the following are true:

1. arbitrary feasible comparison outcomes are modeled over `ℝ` (or an exactly justified equivalent domain);
2. the manuscript's bundle-SD Pareto-improvement definition is represented without denominator or candidate-set restrictions;
3. the continuous OE proof is accepted by Lean with no `sorry`/axiom placeholder introduced for the substantive step;
4. this crosswalk is updated to point to the exact OE theorem declaration.
