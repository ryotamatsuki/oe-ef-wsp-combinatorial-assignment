# Formalization crosswalk

This file prevents a green Lean build from being mistaken for a proof of a differently stated manuscript theorem.

| Canonical source | Mathematical object / claim | Lean declaration | Status |
|---|---|---|---|
| `docs/OPEN_PROBLEM.md` | Three agents, goods `a,b`, unit supplies, bundles `(a,b,ab,empty)`, fractional feasibility only | `Bundle`, `Row`, `Outcome`, `Feasible`, `RealFeasible` | FORMALIZED / AUDITED |
| `src/preferences.py` | Six strict rankings `A,B,E,F,C,D` | `SixType`, `first`, `second`, `third` | FORMALIZED / AUDITED |
| `src/preferences.py` | Bundle-level SD cumulative cutoffs | `cum1`, `cum2`, `cum3`, `SDWeak`; real analogues in `ContinuousOE.lean` | FORMALIZED / AUDITED |
| `src/mechanism_six_type.py` | L/R classification and `k` | `isLeft`, `leftIndicator`, `leftCount` | FORMALIZED / AUDITED |
| `src/mechanism_six_type.py` | Exact six-type allocation table | `tableRow`, `mechanism` | FORMALIZED / AUDITED |
| `theory/six_type_explicit_mechanism.md` | Fractional feasibility | `sixType_feasible` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Envy-freeness under bundle-level SD | `sixType_envyFree` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Full bundle-level SD-strategy-proofness | `sixType_fullSDStrategyProof` | LEAN-CERTIFIED |
| `theory/six_type_explicit_mechanism.md` | Ordinal efficiency against the full continuous fractional feasible set | `sixType_continuous_ordinallyEfficient` | LEAN-CERTIFIED |
| `docs/THEOREM_STATUS.md` T1 | Combined feasibility + OE + EF + full SD-SP theorem | `T1At`, `sixType_T1` | FULLY LEAN-CERTIFIED / GAP-AUDITED |

## Exact counting correspondence

For each of the `6^3 = 216` ordered profiles:

- EF checks 3 agents × 2 other agents × 3 non-trivial SD cutoffs, giving `216 × 18 = 3,888` exact cutoff inequalities.
- Full SD-SP checks 3 agent positions × 6 possible reports. The Lean theorem includes the truthful report as a weak-dominance equality case. Removing the truthful report leaves `216 × 3 × 5 = 3,240` genuine unilateral deviations, matching the canonical Python count.

## Continuous OE scope

The Lean theorem `sixType_continuous_ordinallyEfficient` quantifies over arbitrary real-valued comparison outcomes in the original continuous fractional feasible set. `RealFeasible` imposes exactly componentwise nonnegativity, row probability mass one, and unit capacity for each good, with `ab` consuming one unit of each good. This matches the repository's canonical statement that feasibility is fractional and exact ex-post decomposability is not imposed.

The formalization introduces no denominator restriction, candidate-set restriction, vertex restriction, deterministic-decomposition restriction, anonymity assumption, or neutrality assumption. Bundle-level SD Pareto improvement is represented directly as weak SD improvement for all agents plus a strict improvement at at least one non-trivial cutoff for at least one agent.

## Ranking representation note

Lean stores the first, second, and third bundles for each six-type ranking rather than a separate fourth-coordinate function. With exactly four bundles and probability mass one, the fourth SD cutoff is identically one and therefore trivial. The omitted fourth bundle is the unique remaining bundle, and the first three bundles match `SIX_TYPE_RANKINGS` type-by-type. This is a representation choice, not a weakening of bundle-level SD.

## Paper-level theorem correspondence

`T1At` is the conjunction of exactly the four properties claimed for the explicit six-type rule at an ordered profile:

1. `Feasible (mechanism t0 t1 t2)`;
2. `EnvyFreeAt t0 t1 t2`;
3. `∀ mis, FullSDStrategyProofAgainst t0 t1 t2 mis`;
4. `ContinuousOrdinallyEfficientAt t0 t1 t2`.

`sixType_T1` proves `T1At t0 t1 t2` for arbitrary `t0 t1 t2 : SixType`, hence for all 216 ordered profiles.

## Audit status

A hostile formalization-gap audit found no substantive mismatch between the canonical repository T1 statement and the Lean theorem. See `docs/T1_LEAN_FORMALIZATION_GAP_AUDIT.md`.
