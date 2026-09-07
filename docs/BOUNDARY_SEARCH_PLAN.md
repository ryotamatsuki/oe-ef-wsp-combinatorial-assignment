# Boundary search plan after the arbitrary-n positive theorem

## Purpose

The arbitrary-n theorem proves existence on the full strict-ranking domain satisfying

`a > empty` and `b > empty`.

With four bundles there are 24 strict rankings. They partition exactly into:

- 8 rankings where both singletons are acceptable;
- 8 rankings where exactly one singleton is unacceptable;
- 8 rankings where both singletons are unacceptable.

Therefore the mathematically minimal way to leave the positive theorem's domain is to add one of the eight one-singleton-unacceptable types.

## Canonical one-singleton-unacceptable mirror classes

Up to swapping goods `a` and `b`, there are four classes:

1. `H_A: a > ab > empty > b`  (mirror `H_B`)
2. `P_A: ab > a > empty > b`  (mirror `P_B`)
3. `U_A: a > empty > ab > b`  (mirror `U_B`)
4. `W_A: a > empty > b > ab`  (mirror `W_B`)

## Completed one-sided boundary attacks

### `D_acc + {H_A}`

**SAT.** Exact finite-domain certificate in `docs/BOUNDARY_ATTACK_1_RESULT.md`.

### `D_acc + {P_A}`

**SAT.** Exact finite-domain certificate in `docs/BOUNDARY_ATTACK_PA_RESULT.md`.

The `P_A` mechanism is especially simple: singleton PS is already feasible, EF, and WSP on all 729 profiles and fails OE only at 13 profiles. A closed-form 13-profile repair gives an exact OE+EF+WSP mechanism with maximum allocation denominator 6 and minimum positive WSP margin `1/6`.

These results rule out the hypothesis that a single adjacent-swap outside-option crossing is enough for impossibility.

## Next stage — mirror-pair crossing

The next frontier is to allow one-singleton-unacceptable reports in both good directions.

Attack in this order:

1. `D_acc + {H_A,H_B}`;
2. if SAT, `D_acc + {P_A,P_B}`;
3. if both SAT, test analogous U/W mirror pairs;
4. only then move to types with both singletons unacceptable.

The mirror-pair step is not redundant with the one-sided result. A mechanism may accommodate one unacceptable direction but fail once WSP links force compatible choices across both `a`- and `b`-oriented crossing types.

## Anchor profiles

### All `H_A`

EF forces equal rows. OE requires `q=0` and full use of the a-capacity:

`p+r=1/n`, `z=1-1/n`.

The split between `p` and `r` is generally not fixed.

### All `P_A`

EF forces equal rows. OE uniquely gives

`(p,q,r,z)=(0,0,1/n,1-1/n)`.

The mirror statements hold for `H_B` and `P_B` after swapping goods.

## Later stage — both singletons unacceptable

If the one-singleton-unacceptable mirror-pair frontier remains SAT, add

`T_A: ab > empty > a > b`,

`T_B: ab > empty > b > a`.

At an all-`T_A` or all-`T_B` profile, OE+EF uniquely forces

`(p,q,r,z)=(0,0,1/n,1-1/n)`.

## Solver rule

Passing the known-good six-type fixture proves only that a solver does not reject that known solution. It does not establish completeness on a new domain.

For every boundary domain:

1. rebuild OE from the original continuous fractional feasible set and bundle-level SD;
2. do not import a domain-specific OE characterization from an earlier domain;
3. treat fixed-grid or incomplete-face UNSAT as nonconclusive;
4. verify SAT mechanisms independently with exact arithmetic;
5. verify any UNSAT with a complete second formulation and an explicit proof/certificate.

## Current next domain

`D_MIRROR_H = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`.
