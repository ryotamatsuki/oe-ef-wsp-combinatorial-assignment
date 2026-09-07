# Boundary search plan after the arbitrary-n positive theorem

## Purpose

The arbitrary-n theorem proves existence on the full strict-ranking domain satisfying `a > empty` and `b > empty`.

With four bundles there are 24 strict rankings:

- 8 with both singletons acceptable;
- 8 with exactly one singleton unacceptable;
- 8 with both singletons unacceptable.

The search therefore crosses the positive boundary minimally before adding stronger outside-option crossings.

## One-singleton-unacceptable mirror classes

Up to swapping goods:

1. `H_A: a > ab > empty > b` / `H_B`;
2. `P_A: ab > a > empty > b` / `P_B`;
3. `U_A: a > empty > ab > b` / `U_B`;
4. `W_A: a > empty > b > ab` / `W_B`.

## Completed attacks

- `D_acc + {H_A}`: **SAT**. See `docs/BOUNDARY_ATTACK_1_RESULT.md`.
- `D_acc + {P_A}`: **SAT**. See `docs/BOUNDARY_ATTACK_PA_RESULT.md`.
- `D_acc + {H_A,H_B}`: **SAT**. See `docs/BOUNDARY_ATTACK_H_MIRROR_RESULT.md`.

The H mirror-pair certificate covers 1,000 ordered profiles and 27,000 unilateral deviations exactly. It is WSP but not full SD-SP, confirming that the search must preserve the exact WSP axiom rather than strengthen it.

## Current stage — pair-first mirror crossing

Next attack:

`D_P_MIRROR = D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`.

This is the highest-value remaining adjacent-swap mirror domain because both new types rank `ab` first and one singleton below the outside option. It places the strongest pair-demand pressure on both goods simultaneously while remaining one-singleton-unacceptable.

If `D_P_MIRROR` is SAT:

1. test `D_acc + {U_A,U_B}`;
2. test `D_acc + {W_A,W_B}`;
3. then escalate to both-singletons-unacceptable types.

If `D_P_MIRROR` produces an UNSAT candidate, do not treat fixed-grid or incomplete-face infeasibility as proof. Require a complete continuous formulation and an independent exact certificate.

## Later stage — both singletons unacceptable

Candidate pair:

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

At an all-`T_A` or all-`T_B` profile, OE+EF uniquely forces `(p,q,r,z)=(0,0,1/n,1-1/n)`.

## Solver rule

For every new boundary domain:

1. rebuild OE from the original continuous fractional feasible set and bundle-level SD;
2. do not import a domain-specific OE characterization from an earlier domain;
3. treat fixed-grid or incomplete-face UNSAT as nonconclusive;
4. verify SAT mechanisms independently with exact arithmetic;
5. verify any UNSAT with a complete second formulation and an explicit proof/certificate.

## Current next domain

`D_P_MIRROR = D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`.
