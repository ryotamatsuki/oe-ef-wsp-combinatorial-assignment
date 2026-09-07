# Boundary attack — P_A/P_B mirror-pair result

## Domain

`D_P_MIRROR = D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}`

with

- `P_A: ab > a > empty > b`;
- `P_B: ab > b > empty > a`.

Three agents, two unit-supply goods, fractional feasibility, bundle-level SD.

## Singleton-PS diagnostic

Singleton probabilistic serial on `(a,b,empty)`, ignoring `ab`, satisfies feasibility, EF, and WSP on all 1,000 ordered profiles, but fails OE at exactly 26 ordered profiles.

The failures are exactly the union of the one-sided `P_A` failure classes and their exact good-swap mirrors:

- permutations of `(A,P_A,P_A)`, `(E,P_A,P_A)`, `(C,P_A,P_A)`, `(J,P_A,P_A)`, plus `(P_A,P_A,P_A)`;
- permutations of `(B,P_B,P_B)`, `(F,P_B,P_B)`, `(D,P_B,P_B)`, `(K,P_B,P_B)`, plus `(P_B,P_B,P_B)`.

No additional cross-coupled OE failure appears at profiles mixing `P_A` and `P_B`.

## Closed-form repair

Keep singleton PS on the other 974 profiles.

For the `P_A` side, use the previously certified one-sided repair:

- at permutations of `(X,P_A,P_A)` for `X in {A,E,J}`, give `X` the mixed row `(1/3,1/3,0,1/3)` and each `P_A` the pair row `(0,0,1/3,2/3)`;
- at permutations of `(C,P_A,P_A)` and at `(P_A,P_A,P_A)`, give every agent `(0,0,1/3,2/3)`.

For the `P_B` side, apply the exact `a <-> b` mirror:

- at permutations of `(X,P_B,P_B)` for `X in {B,F,K}`, give `X` `(1/3,1/3,0,1/3)` and each `P_B` `(0,0,1/3,2/3)`;
- at permutations of `(D,P_B,P_B)` and at `(P_B,P_B,P_B)`, give every agent `(0,0,1/3,2/3)`.

This changes exactly 26 ordered profiles relative to singleton PS.

## Exact verification

The repaired mechanism satisfies:

- profiles: 1,000;
- changed profiles: 26;
- feasibility: exact PASS;
- EF cutoff inequalities: 18,000 exact PASS;
- unilateral deviations: 27,000 exact WSP PASS;
- WSP equality deviations: 8,376;
- minimum positive WSP margin: `1/6`;
- maximum allocation denominator: 6.

## Exact continuous OE certificate

The verifier reconstructs the original 9-dimensional fractional feasible polytope exactly from its 14 facet inequalities and obtains exactly 22 vertices.

For every one of the 1,000 profiles it searches strictly positive rational weights on the nine non-trivial bundle-SD cumulative criteria. Denominators 9 through 15 suffice for every profile.

Each mechanism allocation weakly maximizes the corresponding positive scalarization against all 22 vertices. Hence every allocation is OE on the original continuous fractional feasible set, not merely on a candidate grid or incomplete face library.

Certificate bounds:

- minimum support weight: `1/15`;
- maximum support-weight denominator: 15;
- support verification uses exact `Fraction` arithmetic.

Implementation: `src/boundary_p_mirror_certificate.py`.
Permanent test: `tests/test_boundary_p_mirror_certificate.py`.

## Verdict

`D8_ACCEPTABLE_SINGLETONS + {P_A,P_B}` is **CONTINUOUS SAT**.

Thus both adjacent-swap one-singleton-unacceptable mirror families tested so far, H and P, remain compatible with OE+EF+WSP for three agents.

## Search escalation

At this point, continuing indefinitely one mirror class at a time has diminishing value. The next high-value computational target should increase granularity:

`D16_ONE_SINGLETON_ACCEPTABLE =` all 16 strict rankings in which at least one singleton is ranked above the outside option.

Equivalently, combine the eight acceptable-singleton rankings with all eight one-singleton-unacceptable rankings `{H_A,H_B,P_A,P_B,U_A,U_B,W_A,W_B}`.

If this 16-type domain is SAT, it strongly supports a larger positive-domain conjecture: coexistence may hold whenever at least one singleton is acceptable. If it is UNSAT, extract the smallest responsible type subset from this complete one-singleton-unacceptable frontier.

Any UNSAT claim still requires a complete continuous formulation and an independent exact certificate; fixed-grid or incomplete-face infeasibility is not proof.
