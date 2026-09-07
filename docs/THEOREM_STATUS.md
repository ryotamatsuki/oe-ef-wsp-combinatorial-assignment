# Theorem status

## T1 — Six-type explicit existence theorem

**Status: VERIFIED RESTRICTED-DOMAIN THEOREM.**

Domain `D†={A,B,E,F,C,D}` with full strict rankings as defined in `src/preferences.py`. For three agents and two unit-supply goods, the explicit rule in `theory/six_type_explicit_mechanism.md` satisfies fractional feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

Evidence: 216 profiles, 3,888 non-trivial EF cutoff inequalities, 3,240 unilateral deviations, analytic OE proof over the full continuous fractional feasible set, and independent numerical self-attack.

## T2 — Arbitrary-n, two-good acceptable-singletons existence theorem

**Status: ANALYTICALLY CLOSED / FROZEN POSITIVE THEOREM.**

For every `n>=2`, two unit-supply goods `a,b`, and the full strict-ranking domain satisfying `a > empty` and `b > empty`, there exists an explicit fractional mechanism satisfying feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

The proof in `theory/arbitrary_n_two_goods.md` is fully analytic and works against the original continuous fractional feasible set.

## T3 — One-sided H crossing

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, `D_H = D8_ACCEPTABLE_SINGLETONS + {H_A}`, where `H_A: a > ab > empty > b`, admits an exact rational OE+EF+WSP mechanism on all 729 ordered profiles. See `docs/BOUNDARY_ATTACK_1_RESULT.md` and `src/boundary1_certificate.py`.

## T4 — One-sided pair-first crossing

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, `D_PA = D8_ACCEPTABLE_SINGLETONS + {P_A}`, where `P_A: ab > a > empty > b`, admits a closed-form OE+EF+WSP mechanism on all 729 ordered profiles.

Certificate facts: 13,122 EF cutoffs PASS, 17,496 deviations WSP PASS, minimum positive WSP margin `1/6`, maximum allocation denominator 6, exact 22-vertex continuous feasible polytope, and positive rational SD-support weights with denominator at most 15. See `docs/BOUNDARY_ATTACK_PA_RESULT.md` and `src/boundary2_pa_certificate.py`.

## T5 — Two-sided H mirror crossing

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, define

`D_H_MIRROR = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`

with

- `H_A: a > ab > empty > b`;
- `H_B: b > ab > empty > a`.

A closed-form repair of singleton PS satisfies feasibility, OE, EF, and WSP on all `10^3=1,000` ordered profiles.

The mechanism changes singleton PS at exactly 12 ordered profiles: permutations of `(X,H_A,H_A)` and `(X,H_B,H_B)` for `X in {C,D}`.

Certificate facts:
- 1,000 profiles;
- 18,000 non-trivial EF cutoff inequalities: exact PASS;
- 27,000 ordered unilateral deviations: exact WSP PASS;
- 8,328 WSP equality deviations;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6;
- the original continuous feasible polytope is reconstructed exactly from 14 facets and has 22 vertices;
- every profile has a strictly positive rational SD-support vector with denominator at most 14;
- minimum support weight: `1/14`.

The mechanism is WSP but not full SD-strategy-proof; this distinction is explicitly regression-tested. See `docs/BOUNDARY_ATTACK_H_MIRROR_RESULT.md`, `src/boundary_h_mirror_certificate.py`, and `tests/test_boundary_h_mirror_certificate.py`.

## Boundary implication

T2 gives the clean analytic positive domain. T3 and T4 show that one-sided adjacent-swap outside-option crossing remains SAT. T5 shows that even two-sided H-type mirror crossing remains SAT.

The next frontier is the pair-first mirror domain

`D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`.

If that is also SAT, test the remaining one-singleton-unacceptable U/W mirror pairs before escalating to types with both singletons below the outside option.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
