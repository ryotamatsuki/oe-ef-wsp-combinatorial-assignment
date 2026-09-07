# Boundary attack — H_A/H_B mirror-pair result

## Domain

`D_H_MIRROR = D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`

with

- `H_A: a > ab > empty > b`;
- `H_B: b > ab > empty > a`.

Three agents, two unit-supply goods, fractional feasibility, bundle-level SD.

## Singleton-PS diagnostic

Singleton probabilistic serial on `(a,b,empty)`, ignoring `ab`, satisfies:

- feasibility on all 1,000 profiles;
- EF on all 1,000 profiles;
- WSP on all 27,000 ordered unilateral deviations;
- OE fails at exactly 6 profiles.

The six OE failures are the three permutations of `(C,H_A,H_A)` and the three permutations of `(D,H_B,H_B)`.

## Closed-form repair

Keep singleton PS at every other profile.

At any permutation of `(X,H_A,H_A)` for `X in {C,D}` assign

- `X: (a,b,ab,empty)=(0,2/3,1/3,0)`;
- each `H_A: (1/3,0,0,2/3)`.

At any permutation of `(X,H_B,H_B)` for `X in {C,D}` assign

- `X: (2/3,0,1/3,0)`;
- each `H_B: (0,1/3,0,2/3)`.

This changes exactly 12 ordered profiles relative to singleton PS.

## Exact verification

The repaired mechanism satisfies:

- profiles: 1,000;
- changed profiles: 12;
- feasibility: exact PASS;
- EF cutoff inequalities: 18,000 exact PASS;
- unilateral deviations: 27,000 exact WSP PASS;
- WSP equality deviations: 8,328;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6.

## Exact continuous OE certificate

The verifier reconstructs the original 9-dimensional fractional feasible polytope exactly from its 14 facets and obtains exactly 22 vertices.

For every one of the 1,000 profiles it searches positive rational weights on the nine non-trivial bundle-SD cumulative criteria. Denominators 9 through 14 suffice. Every profile has a strictly positive support vector such that the mechanism allocation weakly maximizes the weighted sum against all 22 vertices.

Therefore each allocation is OE on the original continuous fractional feasible set, not merely on a candidate grid or incomplete face library.

Certificate bounds:

- minimum support weight: `1/14`;
- maximum support-weight denominator: 14;
- support verification uses exact rational arithmetic.

Implementation: `src/boundary_h_mirror_certificate.py`.
Permanent test: `tests/test_boundary_h_mirror_certificate.py`.

## WSP versus full SD-strategy-proofness

The mechanism is WSP but not full SD-SP. For example at `(A,A,H_B)`, agent 1 of true type A receives cumulative vector

`(1/2,2/3,1)`.

If it reports B, its cumulative vector under true type A becomes

`(1/4,3/4,1)`.

The first cutoff worsens while the second improves. Thus the misreport does not strictly SD-dominate truth, so WSP holds, but truth also does not weakly SD-dominate the misreport, so full SD-SP fails.

This distinction is intentional and matches the open problem's WSP requirement.

## Verdict

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}` is **CONTINUOUS SAT**.

Two-sided one-singleton-unacceptable crossing of the H-type does not generate impossibility.

## Next target

Proceed to the pair-first mirror domain

`D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`.

If that domain is also SAT, the next escalation is to the remaining one-singleton-unacceptable mirror classes and then to both-singletons-unacceptable types.
