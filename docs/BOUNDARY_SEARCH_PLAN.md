# Boundary search plan after the arbitrary-n positive theorem

## Purpose

The arbitrary-n theorem proves existence on the full strict-ranking domain satisfying

`a > empty` and `b > empty`.

With four bundles there are 24 strict rankings. They partition exactly into:

- 8 rankings where both singletons are acceptable;
- 8 rankings where exactly one singleton is unacceptable;
- 8 rankings where both singletons are unacceptable.

Therefore the mathematically minimal way to leave the positive theorem's domain is to add **one** of the eight one-singleton-unacceptable types.

## Canonical one-singleton-unacceptable mirror classes

Up to swapping goods `a` and `b`, there are four classes:

1. `H_A: a > ab > empty > b`  (mirror `H_B`)
2. `P_A: ab > a > empty > b`  (mirror `P_B`)
3. `U_A: a > empty > ab > b`  (mirror `U_B`)
4. `W_A: a > empty > b > ab`  (mirror `W_B`)

`H_A` is the old working type `H`. `T_A` below is the old `G1` type.

## Boundary Attack 1 — minimal single-type extensions

Start with one added type at a time:

- `D_acc + {H_A}`;
- `D_acc + {P_A}`;
- `D_acc + {U_A}`;
- `D_acc + {W_A}`.

Single mirror additions need not be duplicated computationally because the domains are isomorphic under relabeling `a <-> b`; this is a domain-isomorphism argument, not a neutrality assumption on an unknown mechanism.

The first two are especially sharp because they cross the positive-theorem boundary by a single adjacent swap with an acceptable-domain type:

- `E: a > ab > b > empty` -> `H_A: a > ab > empty > b`;
- `C: ab > a > b > empty` -> `P_A: ab > a > empty > b`.

## Boundary Attack 1b — symmetric pair extensions

If the single-type extensions are SAT, add mirror pairs:

- `D_acc + {H_A,H_B}`;
- `D_acc + {P_A,P_B}`;
- then the analogous U/W pairs.

This tests whether impossibility arises only when outside-option crossing occurs in both good directions simultaneously.

## Anchor profiles

These profiles are useful analytic sanity checks for any new OE representation.

### All `H_A`

At the identical-type profile, EF forces equal rows. OE requires `q=0` and full use of the a-capacity:

`p+r=1/n`, `z=1-1/n`.

The split between `p` and `r` is generally not fixed. A correct solver must allow this continuum.

### All `P_A`

At the identical-type profile, EF forces equal rows. OE uniquely gives

`(p,q,r,z)=(0,0,1/n,1-1/n)`.

If `r<1/n`, either empty mass can be moved to `ab`, or positive `a` mass can be upgraded to `ab` using unused b-capacity.

### All `U_A` or all `W_A`

The singleton `a` is the only acceptable nonempty singleton outcome; `ab` and/or `b` lie below the outside option. OE+EF forces the canonical singleton-only equal allocation

`(p,q,r,z)=(1/n,0,0,1-1/n)`.

These anchors must be checked directly against the original bundle-SD improvement problem; the six-type OE characterization must not be reused.

## Boundary Attack 2 — both singletons unacceptable

If the one-singleton-unacceptable frontier remains SAT, add

`T_A: ab > empty > a > b`,

`T_B: ab > empty > b > a`.

Define

`D_next = D_acc + {T_A,T_B}`.

At an all-`T_A` or all-`T_B` profile, OE+EF uniquely forces

`(p,q,r,z)=(0,0,1/n,1-1/n)`.

This creates the opposite anchor from the positive theorem, where `ab=0` was always optimal for the constructed mechanism.

## Solver rule

Passing the known-good six-type fixture proves only that a solver does not reject that known solution. It does **not** establish completeness on a new domain.

For every boundary domain:

1. rebuild OE from the original continuous fractional feasible set and bundle-level SD;
2. do not import the six-type OE face characterization;
3. treat fixed-grid or incomplete-face UNSAT as nonconclusive;
4. verify SAT mechanisms independently and verify any UNSAT with a complete second formulation/certificate.

## Current next domain

The first recommended computational/analytic boundary domain is

`D_BOUNDARY_1 = D8_ACCEPTABLE_SINGLETONS + {H_A}`.

In parallel, `D8_ACCEPTABLE_SINGLETONS + {P_A}` is the highest-value pair-first comparator.
