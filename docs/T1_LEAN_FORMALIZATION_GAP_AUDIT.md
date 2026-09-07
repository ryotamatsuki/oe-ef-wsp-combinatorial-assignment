# T1 Lean Formalization-Gap Hostile Audit

Date: 2026-09-08 (Asia/Tokyo)

## Verdict

**PASS — NO SUBSTANTIVE FORMALIZATION GAP FOUND.**

The canonical T1 statement in `theory/six_type_explicit_mechanism.md` and `docs/THEOREM_STATUS.md` is faithfully represented by the Lean formalization. The paper-level claim is now represented by the single combined declaration `OEEFWSP.sixType_T1` proving `OEEFWSP.T1At` for every ordered six-type profile.

This verdict is limited to the canonical repository T1 statement. It does not certify novelty, economic significance, or any later manuscript wording that departs from the canonical definitions audited here.

## Authority audited

- Environment and methodological scope: `docs/OPEN_PROBLEM.md`
- Six strict rankings and bundle order: `src/preferences.py`
- Explicit mechanism: `src/mechanism_six_type.py`
- Canonical T1 proof: `theory/six_type_explicit_mechanism.md`
- Canonical theorem status: `docs/THEOREM_STATUS.md`
- Lean definitions and finite proofs: `formal/lean/OEEFWSP/Basic.lean`, `formal/lean/OEEFWSP/SixType.lean`
- Lean continuous OE proof: `formal/lean/OEEFWSP/ContinuousOE.lean`
- Combined paper-level theorem: `formal/lean/OEEFWSP/T1.lean`

## Hostile checks

| Risk | Audit result |
|---|---|
| Wrong agent/good environment | PASS. Lean fixes three agents, goods `a,b`, and unit capacities exactly as canonical T1. |
| Wrong bundle set | PASS. Lean uses exactly `a,b,ab,empty`; `ab` consumes one unit of each good. |
| Hidden ex-post implementability | PASS. `Feasible`/`RealFeasible` impose fractional row and capacity constraints only; no deterministic decomposability is imposed. |
| Hidden denominator restriction | PASS. Continuous OE comparison allocations are over `ℝ`. |
| Hidden candidate/grid/vertex restriction | PASS. `ContinuousOrdinallyEfficientAt` universally quantifies over arbitrary real feasible outcomes. |
| Preference-domain mismatch | PASS. `SixType={A,B,E,F,C,D}` and the first three ranked bundles match `SIX_TYPE_RANKINGS` type-by-type; the fourth bundle is the unique remaining bundle. |
| Marginal SD substituted for bundle SD | PASS. SD cutoffs are cumulative probabilities over ranked bundles. |
| Missing SD cutoff | PASS. For four bundles there are exactly three non-trivial cutoffs; the fourth cumulative probability is one for feasible lottery rows. |
| EF direction reversed | PASS. Each agent's own row is required to weakly SD-dominate every other agent's row under that agent's true type. |
| WSP/full SD-SP confusion | PASS. T1 proves the stronger full bundle-level SD-strategy-proofness: truth weakly SD-dominates every unilateral misreport. |
| Misreport quantification incomplete | PASS. `sixType_fullSDStrategyProof` is universal in the misreport type and covers each of the three agent positions. |
| Mechanism table mismatch | PASS. All reachable `k=0,1,2,3` L/R rows exactly match the Python and theory table. The total-function fallback branch is unreachable on six-type profiles. |
| OE weak/strict Pareto definition mismatch | PASS. Lean requires weak SD improvement for every agent and strict improvement at at least one non-trivial cutoff for at least one agent. |
| Baseline feasibility omitted from paper-level theorem | CLOSED. Continuous OE is a separate predicate, while `T1At` explicitly conjoins feasibility with OE, EF, and full SD-SP. |
| Analytic OE replaced by finite search | PASS. The Lean OE theorem proves nonexistence of a dominating arbitrary real-valued feasible allocation; no finite candidate enumeration is used. |
| `sorry` / substantive axiom placeholder | PASS on the audited Lean source. The substantive T1 proof is explicit and the project is required to pass `lake build --wfail`. |
| Python/Lean arithmetic mismatch | PASS. Finite mechanism values are exact rationals in Lean; the OE comparison domain is explicitly cast to reals. |

## Proof-scope correspondence

The paper-level T1 claim is:

1. fractional feasibility;
2. bundle-level envy-freeness;
3. full bundle-level SD-strategy-proofness;
4. ordinal efficiency against the original continuous fractional feasible set.

Lean now defines

`T1At t0 t1 t2 := Feasible(...) ∧ EnvyFreeAt(...) ∧ (∀ mis, FullSDStrategyProofAgainst(...,mis)) ∧ ContinuousOrdinallyEfficientAt(...)`

and proves

`theorem sixType_T1 (t0 t1 t2 : SixType) : T1At t0 t1 t2`.

Because `t0,t1,t2` are arbitrary elements of the six-type inductive domain, this covers all `6^3=216` ordered profiles.

## Non-gaps noted explicitly

### Fourth-ranked bundle is implicit

Lean records the first three ranked bundles because stochastic dominance over four outcomes has only three non-trivial cutoffs. The canonical fourth bundle is the unique remaining bundle. Since all relevant lottery rows have probability mass one, the fourth cutoff adds only the identity `1 ≥ 1`. This does not weaken SD, EF, SP, or OE.

### Continuous OE theorem does not itself assert baseline feasibility

`ContinuousOrdinallyEfficientAt` is intentionally a no-improvement predicate. Baseline feasibility is certified separately by `sixType_feasible` and conjoined in the paper-level `T1At` theorem. Thus the combined theorem matches the standard feasible-and-undominated T1 claim.

### Lean proof route differs from prose proof route

The prose proof sometimes concludes the dominating allocation must equal the benchmark. The Lean proof only derives the contradiction needed to rule out a strict SD-Pareto improvement. This is logically sufficient for OE and proves the same theorem; proof-text identity is not required.

## Freeze rule

T1 may be treated as formally frozen once the PR containing `T1At` / `sixType_T1` and this audit passes both:

- GitHub Actions `Lean formal verification` (`lake build --wfail`), and
- the existing Python regression suite.

After freeze, changes to any of the following invalidate the audit and require a new formalization-gap audit: six-type rankings, L/R classification, mechanism table, feasibility definition, bundle-SD definition, EF definition, strategy-proofness notion, continuous OE definition, or T1 theorem wording.
