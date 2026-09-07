# Boundary attack — complete 16-type frontier result

## Domain

`D16_ONE_SINGLETON_ACCEPTABLE`

is the set of all 16 strict rankings over `{a,b,ab,empty}` for which at least one singleton is ranked above the outside option.

Equivalently:

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

Three agents, two unit-supply goods, fractional feasibility, bundle-level stochastic dominance.

## Initial singleton-PS diagnostic

Singleton probabilistic serial on `(a,b,empty)`, ignoring `ab`, has:

- feasibility: PASS on all 4,096 ordered profiles;
- EF: PASS on all 4,096 profiles;
- WSP: PASS on all 184,320 ordered unilateral deviations;
- OE failure at 296 ordered profiles, grouped into 64 agent-permutation classes.

All 296 OE failures lie entirely within one orientation: either all reports are a-oriented or all are their exact b-oriented mirrors. Mixed-orientation profiles introduce no new singleton-PS OE failure.

## Closed-form repair architecture

The final mechanism keeps singleton PS except on a sparse family of pair-upgrade profiles.

Write

- `S_A={H_A,U_A,W_A}`, `Q_A=S_A union {P_A}`;
- `S_B={H_B,U_B,W_B}`, `Q_B=S_B union {P_B}`.

The repair has four symmetric components.

### 1. Pure A-side repair

If all reports are in `Q_A` and at least one is `P_A`, every `P_A` receives `(0,0,1/3,2/3)` and every other A-side unacceptable type receives `(1/3,0,0,2/3)`.

If exactly two reports are in `Q_A` and the third is an ordinary A-oriented acceptable type `A,E,J`, the number of `P_A` reports determines the residual b-share assigned to that acceptable type.

If the third type is `C`, C receives `ab=1/3` plus the residual b-capacity. The B-side case is the exact good-swap mirror.

### 2. Cross C/D repair

At a profile containing one C and two reports from `Q_B`, let `m` be the number of `P_B` reports. Assign

`C: ((2-m)/3, 0, 1/3, m/3)`,

each `P_B: (0,0,1/3,2/3)`,

and each remaining type in `S_B: (0,1/3,0,2/3)`.

For D plus two reports from `Q_A`, use the exact mirror:

`D: (0,(2-m)/3,1/3,m/3)`.

### 3. Cross P_A/P_B repair

At a profile containing one `P_B` and two reports from `Q_A`, let `m` be the number of `P_A` reports. Assign

`P_B: (0,(2-m)/3,1/3,m/3)`,

each `P_A: (0,0,1/3,2/3)`,

and each remaining type in `S_A: (1/3,0,0,2/3)`.

The `P_A + two Q_B` case is the exact mirror.

### 4. Everywhere else

Use singleton PS unchanged.

The implementation is `src/boundary16_certificate.py`.

## Exact verification

The resulting mechanism satisfies:

- ordered profiles: 4,096;
- profiles changed relative to singleton PS: 488;
- feasibility: exact PASS;
- non-trivial EF cutoff inequalities: 73,728 exact PASS;
- ordered unilateral deviations: 184,320 exact WSP PASS;
- WSP equality deviations: 44,400;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6.

The mechanism is WSP but not full SD-strategy-proof. For example, at `(A,A,H_B)`, an A-agent has truthful cumulative vector `(1/2,2/3,1)` and obtains `(1/4,3/4,1)` after reporting B. The vectors cross, so the misreport does not strictly SD-dominate truth, but truth also does not weakly SD-dominate the misreport.

## Exact continuous OE certificate

The original 9-dimensional fractional feasible polytope is reconstructed from its 14 facets and has exactly 22 vertices.

For every ordered profile, a strictly positive rational weight vector on the nine non-trivial bundle-SD cumulative criteria is constructed. Numerical LP is used only to locate a candidate support vector; the rationalized vector is then checked exactly with `Fraction` arithmetic against all 22 vertices.

Across all 4,096 profiles:

- every profile has a valid positive support vector;
- minimum support weight: `1/15`;
- maximum support-weight denominator: 19.

Therefore every allocation is OE on the original continuous fractional feasible set. The result does not rely on a candidate grid, incomplete efficient-face library, or fixed denominator restriction.

## Verdict

`D16_ONE_SINGLETON_ACCEPTABLE` is **CONTINUOUS SAT** for three agents and two goods.

Thus the complete frontier in which at least one singleton is acceptable does not generate the desired impossibility.

## Research implication

This substantially strengthens the positive-domain evidence. The next useful step is no longer another one-singleton-unacceptable subtype. The search should move to preferences where **both** singletons are below the outside option, beginning with

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

Before launching a large negative search, the D16 mechanism should also be examined for an analytic characterization/generalization, but this should be time-boxed: the main open-problem search now belongs on the both-singletons-unacceptable frontier.
