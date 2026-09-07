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

`D_H = D8_ACCEPTABLE_SINGLETONS + {H_A}`

with `H_A: a > ab > empty > b`.

An exact rational mechanism exists satisfying feasibility, OE, EF, and WSP on all `9^3=729` ordered profiles.

Certificate facts:
- 729 profiles;
- 13,122 non-trivial EF cutoff inequalities: exact PASS;
- 17,496 ordered unilateral deviations: exact WSP PASS;
- 5,970 deviations use the WSP equality branch;
- minimum positive WSP margin among non-equality deviations: `1/1000`;
- maximum allocation denominator: 12,000;
- every allocation is supported as OE by strictly positive bundle-SD criterion weights and checked against all 22 vertices of the original fractional feasible polytope.

Consequently, adding a single `H_A` type does **not** generate impossibility.

## T4 — Pair-first minimal outside-option crossing extension

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, define

`D_PA = D8_ACCEPTABLE_SINGLETONS + {P_A}`

with `P_A: ab > a > empty > b`.

A closed-form repair of singleton PS exists satisfying feasibility, OE, EF, and WSP on all 729 ordered profiles.

The mechanism differs from singleton PS at only 13 profiles: the permutations of `(X,P_A,P_A)` for `X in {A,E,C,J}` and `(P_A,P_A,P_A)`.

Certificate facts:
- 729 profiles;
- 13,122 non-trivial EF cutoff inequalities: exact PASS;
- 17,496 ordered unilateral deviations: exact WSP PASS;
- 6,204 WSP equality deviations;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6;
- the original continuous feasible polytope is reconstructed exactly from 14 facets and has 22 vertices;
- every profile has a strictly positive rational SD-support vector with denominator at most 15;
- minimum support weight: `1/15`;
- OE support verification is exact rational arithmetic and does not rely on candidate-face completeness or floating LP output.

The certificate is implemented in `src/boundary2_pa_certificate.py` and tested in `tests/test_boundary2_pa_certificate.py`.

Consequently, the pair-first one-singleton-unacceptable type `P_A` alone is also not an impossibility core.

## Boundary implication

T2 identifies the clean analytic positive domain. T3 and T4 show that crossing that boundary in one direction by either adjacent-swap type `H_A` or `P_A` still permits OE+EF+WSP for three agents.

The next frontier is **two-sided outside-option crossing**, beginning with the mirror-pair domain

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`,

followed, if SAT, by

`D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`.

Only after the one-singleton-unacceptable mirror-pair frontier is mapped should the search move to types with both singletons below the outside option.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
