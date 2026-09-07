# Theorem status

## T1 — Six-type explicit existence theorem

**Status: VERIFIED RESTRICTED-DOMAIN THEOREM.**

Domain `D†={A,B,E,F,C,D}` with full strict rankings as defined in `src/preferences.py`.
For three agents and two unit-supply goods, the explicit rule in `theory/six_type_explicit_mechanism.md` satisfies fractional feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

Evidence:
- exact rational checks of all 216 profiles;
- exact rational checks of all 3,888 non-trivial EF cutoff inequalities;
- exact rational checks of all 3,240 ordered unilateral deviations;
- analytic OE proof over the full continuous fractional feasible set;
- numerical LP self-attack over the original continuous feasible set as corroboration only.

## T2 — Arbitrary-n, two-good acceptable-singletons existence theorem

**Status: ANALYTICALLY CLOSED / FROZEN POSITIVE THEOREM.**

For every `n>=2`, two unit-supply goods `a,b`, and the full strict-ranking domain satisfying

`a > empty` and `b > empty`,

there exists an explicit fractional mechanism satisfying feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

The rule gives every agent total nonempty probability `2/n`, zero probability of `ab`, outside probability `1-2/n`, and uses a closed-form two-singleton eating allocation based only on whether the report has `a>b` or `b>a`.

The proof in `theory/arbitrary_n_two_goods.md` is fully analytic and works against the original continuous fractional feasible set.

## T3 — First minimal outside-option crossing extension

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, define

`D_BOUNDARY_1 = D8_ACCEPTABLE_SINGLETONS + {H_A}`

with `H_A: a > ab > empty > b`.

An exact rational mechanism exists satisfying feasibility, OE, EF, and WSP on all `9^3=729` ordered profiles.

Certificate facts:
- 729 profiles;
- 13,122 non-trivial EF cutoff inequalities: exact PASS;
- 17,496 ordered unilateral deviations: exact WSP PASS;
- 5,970 deviations use the WSP equality branch;
- minimum positive WSP margin among non-equality deviations: `1/1000`;
- maximum allocation denominator: 12,000;
- every allocation is supported as OE by strictly positive bundle-SD criterion weights; the support check was independently rationalized and verified against all 22 vertices of the original fractional feasible polytope;
- an independent continuous LP self-attack finds no positive SD-Pareto improvement.

The mechanism is stored in `src/boundary1_certificate.py`. It equals singleton-PS on 693 profiles and uses 36 exact rational exception allocations to repair the local OE/WSP conflict network around `C` and `H_A`.

Consequently, adding a single `H_A` type does **not** generate impossibility. The one-singleton-unacceptable boundary must be pushed further.

## Boundary implication

T2 identifies the clean analytic positive domain. T3 shows that crossing that boundary by the adjacent-swap type `H_A` alone is still compatible with OE+EF+WSP for three agents.

The next candidate is the pair-first one-singleton-unacceptable type

`P_A: ab > a > empty > b`,

followed, if SAT, by mirror-pair extensions such as `{H_A,H_B}` and `{P_A,P_B}`.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
