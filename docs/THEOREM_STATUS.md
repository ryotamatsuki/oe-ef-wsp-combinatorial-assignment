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

For `n=3`, `D_H_MIRROR = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}` admits a closed-form repair of singleton PS satisfying feasibility, OE, EF, and WSP on all 1,000 ordered profiles.

Certificate facts: 18,000 EF cutoffs PASS, 27,000 deviations WSP PASS, 8,328 equality deviations, minimum positive WSP margin `1/6`, maximum allocation denominator 6, exact 22-vertex continuous polytope, and positive SD-support weights with denominator at most 14. The mechanism is WSP but not full SD-SP. See `docs/BOUNDARY_ATTACK_H_MIRROR_RESULT.md`.

## T6 — Two-sided pair-first P mirror crossing

**Status: VERIFIED FINITE-DOMAIN SAT CERTIFICATE.**

For `n=3`, define

`D_P_MIRROR = D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`

with

- `P_A: ab > a > empty > b`;
- `P_B: ab > b > empty > a`.

A symmetric closed-form repair of singleton PS satisfies feasibility, OE, EF, and WSP on all `10^3=1,000` ordered profiles.

The mechanism changes singleton PS at exactly 26 ordered profiles: the 13 one-sided `P_A` repair profiles and their exact `a <-> b` mirrors on the `P_B` side. Profiles mixing `P_A` and `P_B` require no additional repair.

Certificate facts:
- 1,000 profiles;
- 18,000 non-trivial EF cutoff inequalities: exact PASS;
- 27,000 ordered unilateral deviations: exact WSP PASS;
- 8,376 WSP equality deviations;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6;
- the original continuous feasible polytope is reconstructed exactly from 14 facets and has 22 vertices;
- every profile has a strictly positive rational SD-support vector with denominator at most 15;
- minimum support weight: `1/15`.

See `docs/BOUNDARY_ATTACK_P_MIRROR_RESULT.md`, `src/boundary_p_mirror_certificate.py`, and `tests/test_boundary_p_mirror_certificate.py`.

## Boundary implication

T2 gives the clean analytic positive domain. T3–T6 show that one-sided and two-sided adjacent-swap outside-option crossings of both H and pair-first P types remain compatible with OE+EF+WSP for three agents.

The search now increases granularity instead of continuing indefinitely one mirror class at a time. The next target is the complete 16-type domain containing every strict ranking for which **at least one singleton is acceptable**:

`D16_ONE_SINGLETON_ACCEPTABLE = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

If D16 is SAT, investigate an analytic positive-domain theorem. If D16 is UNSAT, extract the smallest responsible subset and verify the impossibility with a complete continuous second formulation and an independent certificate.

Only after this 16-type frontier is mapped should the search move to types with both singletons below the outside option.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
