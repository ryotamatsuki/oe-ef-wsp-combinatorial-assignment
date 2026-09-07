# Boundary search plan after the arbitrary-n positive theorem

## Purpose

The arbitrary-n theorem proves existence on the full strict-ranking domain satisfying `a > empty` and `b > empty`.

With four bundles there are 24 strict rankings:

- 8 with both singletons acceptable;
- 8 with exactly one singleton unacceptable;
- 8 with both singletons unacceptable.

The search crosses the positive boundary minimally, learns the local obstruction structure, and then increases granularity rather than continuing indefinitely one type at a time.

## One-singleton-unacceptable mirror classes

Up to swapping goods:

1. `H_A: a > ab > empty > b` / `H_B`;
2. `P_A: ab > a > empty > b` / `P_B`;
3. `U_A: a > empty > ab > b` / `U_B`;
4. `W_A: a > empty > b > ab` / `W_B`.

## Completed attacks

- `D_acc + {H_A}`: **SAT**.
- `D_acc + {P_A}`: **SAT**.
- `D_acc + {H_A,H_B}`: **SAT**.
- `D_acc + {P_A,P_B}`: **SAT**.

The P mirror-pair mechanism differs from singleton PS at only 26 ordered profiles and has an exact continuous OE certificate using the complete 22-vertex fractional feasible polytope. See `docs/BOUNDARY_ATTACK_P_MIRROR_RESULT.md`.

These results rule out both one-sided and two-sided adjacent-swap outside-option crossing, for the H and pair-first P families, as immediate impossibility cores.

## Current stage — complete one-singleton-unacceptable frontier

Instead of separately testing the U and W mirror pairs first, escalate to the full 16-type domain

`D16_ONE_SINGLETON_ACCEPTABLE = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

This is exactly the set of all strict rankings in which at least one singleton is ranked above the outside option.

### Why this is the right next granularity

The H and P single/mirror results show that local outside-option crossing can be repaired without generating an incentive contradiction. Continuing class-by-class now has diminishing information value. D16 directly tests the emerging structural conjecture:

> OE+EF+WSP may coexist whenever at least one singleton is acceptable.

### D16 protocol

1. Start from singleton PS on `(a,b,empty)` and diagnose feasibility, EF, WSP, and OE over all `16^3=4096` ordered profiles.
2. Classify OE failures by agent-permutation and good-swap symmetry, but do not impose symmetry as an axiom on an unknown mechanism.
3. Attempt sparse/local repair first if the failure set is concentrated.
4. For SAT, require an explicit mechanism and independent exact verification. Use the complete 22-vertex continuous feasible polytope or an equally complete OE certificate.
5. For any UNSAT candidate, do not rely on fixed-grid, fixed-margin, incomplete-face, or one-scalarization infeasibility. Extract a smaller responsible type core and verify with a second complete formulation/certificate.

## After D16

### If D16 is SAT

Promote the conjecture that the 16-type domain may admit a general positive mechanism, and attempt an analytic characterization/generalization before adding both-singletons-unacceptable types.

### If D16 is UNSAT

Run minimal-core extraction inside the eight one-singleton-unacceptable types to identify the smallest preference extension responsible for the contradiction.

### Both-singletons-unacceptable frontier

Only after D16 is mapped, add types such as

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

At an all-`T_A` or all-`T_B` profile, OE+EF uniquely forces `(p,q,r,z)=(0,0,1/n,1-1/n)`, providing the opposite anchor from the acceptable-singletons theorem.

## Solver rule

For every new boundary domain:

1. rebuild OE from the original continuous fractional feasible set and bundle-level SD;
2. do not import a domain-specific OE characterization from an earlier domain;
3. treat fixed-grid or incomplete-face UNSAT as nonconclusive;
4. verify SAT mechanisms independently with exact arithmetic;
5. verify any UNSAT with a complete second formulation and an explicit proof/certificate.

## Current next domain

`D16_ONE_SINGLETON_ACCEPTABLE`.
