# Astra Round 1 — analytic counterexample to the six-type impossibility hypothesis

## Verdict

**NO VALID IMPOSSIBILITY PROOF FOUND.**

Instead, Astra constructed an explicit mechanism on `D†={A,B,E,F,C,D}` satisfying fractional feasibility, ordinal efficiency, envy-freeness, and full bundle-level SD-strategy-proofness. Hence the six-type domain cannot be an impossibility core.

## Mechanism

Let `L={A,E,C}` and `R={B,F,D}`. The rule depends only on the number `k` of L-reports:

| k | L row `(a,b,ab,empty)` | R row `(a,b,ab,empty)` |
|---:|---|---|
| 0 | — | `(1/3,1/3,0,1/3)` |
| 1 | `(2/3,0,0,1/3)` | `(1/6,1/2,0,1/3)` |
| 2 | `(1/2,1/6,0,1/3)` | `(0,2/3,0,1/3)` |
| 3 | `(1/3,1/3,0,1/3)` | — |

The complete proof is normalized in `theory/six_type_explicit_mechanism.md` and `theory/oe_characterization.md`.

## Independent checks incorporated into this repository

- 216 ordered profiles: exact feasibility PASS;
- 3,888 non-trivial EF cutoff comparisons: exact PASS;
- 3,240 ordered unilateral deviations: exact full SD-SP PASS;
- independent continuous LP OE self-attack on all 216 profiles: maximum numerical gain `8.881784197001252e-16`;
- analytic OE proof remains authoritative.

## Consequence for the old solver

Any model that reports the same six-type domain INFEASIBLE, including the historical `delta=1/1000` candidate-face model, is invalid. The legacy implementation is not available, so its line-level root cause is not reconstructed here.
