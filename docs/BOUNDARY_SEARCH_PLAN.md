# Boundary search plan after the complete 16-type SAT result

## Completed positive frontier

The search has now mapped the entire strict-ranking region in which at least one singleton is above the outside option.

Completed SAT domains for `n=3,m=2` include:

- `D_acc + {H_A}`;
- `D_acc + {P_A}`;
- `D_acc + {H_A,H_B}`;
- `D_acc + {P_A,P_B}`;
- the full 16-type domain
  `D16_ONE_SINGLETON_ACCEPTABLE = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

The final D16 mechanism satisfies feasibility, continuous OE, EF, and exact WSP on all 4,096 ordered profiles and 184,320 unilateral deviations. See `docs/BOUNDARY_ATTACK_D16_RESULT.md`.

## Structural conclusion from D16

For three agents and two goods, **one-singleton unacceptability is not enough to generate impossibility**, even when every such strict ranking is admitted simultaneously.

This substantially sharpens the search boundary. The remaining eight strict rankings are exactly those in which both singletons are below the outside option.

## Next frontier — both singletons unacceptable

Start with the mirror pair

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

These types reverse the D16 mechanism's central escape route: neither singleton is acceptable, while `ab` is top-ranked.

At an all-`T_A` or all-`T_B` profile, OE+EF uniquely forces

`(a,b,ab,empty) = (0,0,1/3,2/3)`

for every agent.

This creates a strong anchor profile for WSP chains linking pair-demanding types to the D16 positive mechanism.

## Stage N1 — both-singletons-unacceptable mirror attack

Target domain:

`D18_T_MIRROR = D16_ONE_SINGLETON_ACCEPTABLE + {T_A,T_B}`.

Protocol:

1. Evaluate the D16 mechanism extended naively to `T_A,T_B` and identify which axiom fails first.
2. Use the all-T anchor profiles and one-report neighborhoods to derive forced or sharply bounded allocations analytically.
3. Search for a SAT repair using only allocations verified OE on the original continuous feasible set.
4. If SAT, continue to the remaining six both-singletons-unacceptable rankings.
5. If an UNSAT candidate appears, immediately run minimal-core extraction; do not assume the full 18-type domain is the minimal contradiction.
6. Any impossibility claim must be independently certified with a complete continuous formulation or a human-readable analytic inequality chain.

## Time-boxed positive-theorem side task

The D16 certificate suggests a larger positive-domain theorem may exist, possibly characterizing the domain by the condition that at least one singleton is acceptable.

Do not let this side task displace the main open-problem search. A short analytic generalization attempt is justified; if it does not close quickly, return to Stage N1.

## Solver rule

For every new negative domain:

1. rebuild OE from the original continuous fractional feasible set and bundle-level SD;
2. do not reuse a domain-specific OE characterization outside its proved domain;
3. fixed-grid, fixed-margin, one-scalarization, or incomplete-face infeasibility is nonconclusive;
4. SAT mechanisms must be independently verified with exact arithmetic;
5. UNSAT requires a complete second formulation and preferably a short analytic proof/core.

## Current next domain

`D18_T_MIRROR = D16_ONE_SINGLETON_ACCEPTABLE + {T_A,T_B}`.
