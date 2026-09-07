# Boundary attack — P_A result

## Domain

`D_PA = D8_ACCEPTABLE_SINGLETONS + {P_A}`

with

`P_A: ab > a > empty > b`.

Three agents, two unit-supply goods, fractional feasibility, bundle-level SD.

## Baseline diagnostic

Singleton probabilistic serial on `(a,b,empty)`, ignoring `ab`, has:

- feasibility: PASS on all 729 profiles;
- EF: PASS on all 729 profiles;
- WSP: PASS on all 17,496 ordered deviations;
- OE failure at exactly 13 profiles.

The 13 failures are precisely:

- the three permutations of `(A,P_A,P_A)`;
- the three permutations of `(E,P_A,P_A)`;
- the three permutations of `(C,P_A,P_A)`;
- the three permutations of `(J,P_A,P_A)`;
- `(P_A,P_A,P_A)`.

Thus the failure is concentrated entirely in profiles with at least two `P_A` reports.

## Closed-form repair

Keep singleton PS unchanged on the other 716 profiles.

At `(X,P_A,P_A)` and its permutations with `X in {A,E,J}`, assign

- `X: (a,b,ab,empty)=(1/3,1/3,0,1/3)`;
- each `P_A: (0,0,1/3,2/3)`.

At `(C,P_A,P_A)` and its permutations, and at `(P_A,P_A,P_A)`, assign every agent

`(0,0,1/3,2/3)`.

No other profile is changed.

## Exact verification

The resulting mechanism satisfies:

- profiles: 729;
- changed profiles relative to singleton PS: 13;
- feasibility: exact PASS;
- EF cutoff inequalities: 13,122 exact PASS;
- unilateral deviations: 17,496 exact WSP PASS;
- WSP equality deviations: 6,204;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6.

## Exact continuous OE certificate

OE is not inferred from a finite candidate face library.

The verifier reconstructs the original 9-dimensional continuous feasible polytope from its 14 facet inequalities using exact `Fraction` Gaussian elimination. It obtains exactly 22 vertices.

For each of the 729 profiles, the verifier searches all strictly positive rational SD-weight vectors whose common denominator is between 9 and 15. Equivalently it enumerates positive integer compositions of each denominator into the nine non-trivial bundle-SD criteria.

For every profile it finds a strictly positive weight vector such that the mechanism allocation weakly maximizes the weighted sum of all nine SD cumulative criteria against every one of the 22 vertices. Since the feasible set is the convex hull of those vertices, this is an exact supporting-hyperplane certificate over the original continuous fractional feasible set.

Certificate bounds:

- minimum support weight: `1/15`;
- maximum support-weight denominator: 15;
- support verification uses exact rational arithmetic only.

The implementation is `src/boundary2_pa_certificate.py`; the permanent regression test is `tests/test_boundary2_pa_certificate.py`.

## Verdict

`D8_ACCEPTABLE_SINGLETONS + {P_A}` is **CONTINUOUS SAT**.

Therefore neither adjacent-swap one-singleton-unacceptable extension `H_A` nor `P_A`, taken alone, is an impossibility core.

## Next target

Move from one-sided boundary crossing to mirror-pair crossing. The recommended next domain is

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`,

followed by

`D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`

if the H mirror pair remains SAT.
