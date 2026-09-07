# Theorem status

## T1 — Six-type explicit existence theorem

**Status: VERIFIED RESTRICTED-DOMAIN THEOREM / FULLY LEAN-CERTIFIED.**

Domain `D†={A,B,E,F,C,D}` with full strict rankings as defined in `src/preferences.py`. For three agents and two unit-supply goods, the explicit rule in `theory/six_type_explicit_mechanism.md` satisfies fractional feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

Evidence: 216 profiles, 3,888 non-trivial EF cutoff inequalities, 3,240 unilateral deviations, independent numerical self-attack, and Lean kernel verification of feasibility, EF, full bundle-level SD-strategy-proofness, and continuous OE. The Lean OE theorem quantifies over arbitrary real-valued feasible comparison outcomes and introduces no denominator, candidate-set, vertex, or deterministic-decomposition restriction.

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

For `n=3`, `D_P_MIRROR = D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}` admits a symmetric closed-form repair of singleton PS satisfying feasibility, OE, EF, and WSP on all 1,000 ordered profiles.

Certificate facts: 18,000 EF cutoffs PASS, 27,000 deviations WSP PASS, 8,376 equality deviations, minimum positive WSP margin `1/6`, maximum allocation denominator 6, exact 22-vertex continuous polytope, and positive rational SD-support weights with denominator at most 15. See `docs/BOUNDARY_ATTACK_P_MIRROR_RESULT.md`.

## T7 — Complete 16-type one-singleton-acceptable frontier

**Status: VERIFIED FINITE-DOMAIN CONTINUOUS SAT CERTIFICATE.**

For `n=3`, let `D16_ONE_SINGLETON_ACCEPTABLE` be the complete set of all 16 strict rankings over `{a,b,ab,empty}` in which at least one singleton is ranked above the outside option:

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

A closed-form repair of singleton PS satisfies feasibility, OE, EF, and WSP on all `16^3=4,096` ordered profiles.

Certificate facts:
- 4,096 ordered profiles;
- 488 profiles changed relative to singleton PS;
- 73,728 non-trivial EF cutoff inequalities: exact PASS;
- 184,320 ordered unilateral deviations: exact WSP PASS;
- 44,400 WSP equality deviations;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6;
- the original continuous fractional feasible polytope is reconstructed exactly and has 22 vertices;
- every profile has a strictly positive rational SD-support vector checked exactly against all 22 vertices;
- minimum support weight: `1/15`;
- maximum support-weight denominator: 19.

The mechanism is WSP but not full SD-strategy-proof. See `docs/BOUNDARY_ATTACK_D16_RESULT.md`, `src/boundary16_certificate.py`, and `tests/test_boundary16_certificate.py`.

## Boundary implication

T2 gives a clean arbitrary-n positive theorem when both singletons are acceptable. T3–T7 show that for three agents the positive region extends much further: **every strict ranking with at least one singleton above the outside option can be accommodated simultaneously**.

This rules out the entire one-singleton-unacceptable frontier as an impossibility source for `n=3,m=2`.

The next negative-search frontier is therefore preferences with **both singletons below the outside option**, beginning with

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

The D16 mechanism may merit a short analytic generalization attempt, but the unrestricted JET open problem remains unresolved and the main negative search should now move to the both-singletons-unacceptable frontier.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
