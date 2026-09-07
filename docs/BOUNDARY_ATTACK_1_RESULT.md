# Boundary Attack 1 — result

## Domain

`D_BOUNDARY_1 = D8_ACCEPTABLE_SINGLETONS + {H_A}`

with

`H_A: a > ab > empty > b`.

Three agents, two unit-supply goods, full fractional feasibility, bundle-level SD.

## Initial diagnostic

The arbitrary-n acceptable-singletons rule remains feasible, EF, and full SD-strategy-proof on this 9-type domain, but it is not OE. Among the 729 ordered profiles, 169 admit an SD-Pareto improvement under that old rule. The first simple failure is `(A,A,H_A)`: replacing the H-agent's positive b probability by outside option strictly improves H without hurting anyone.

A singleton-PS baseline (run only on `a,b,empty`) improves the situation substantially:

- feasibility: PASS on all 729 profiles;
- EF: PASS on all 729 profiles;
- WSP: PASS on all 17,496 ordered deviations;
- OE fails only at the three permutations of `(C,H_A,H_A)`.

At `(C,H_A,H_A)`, singleton-PS gives C `(1/3,2/3,0,0)`. Replacing C's `1/3` of a by `1/3` of `ab` yields `(0,2/3,1/3,0)` and strictly improves C while leaving both H-agents unchanged.

A naive repair only at these three profiles creates a WSP problem through nearby D-to-C reports, so the repair must be done on a small report-connected neighborhood rather than profile by profile.

## Local exact core check

The subdomain `{C,D,H_A}` was solved directly with continuous supported-OE, EF, and exact WSP branch constraints.

Result: **SAT** on all 27 profiles and 162 ordered deviations. The rationalized certificate passes exact feasibility, EF, WSP, and positive-support OE checks.

Thus `{C,D,H_A}` is not an impossibility core.

## Full 9-type repair

Keep singleton-PS fixed on profiles outside the one-report neighborhood of the three OE failures. This fixes 659 profiles. Allow the remaining 70 profiles to vary, with:

- original fractional feasibility;
- EF;
- continuous supported-OE using strictly positive bundle-SD weights;
- WSP disjunctions for every deviation touching the variable neighborhood.

The resulting MILP is SAT. After rational reconstruction, only 36 profiles differ from singleton-PS.

The exact mechanism is stored in `src/boundary1_certificate.py`.

## Independent verification

Exact rational verification gives:

- profiles: 729;
- EF cutoff inequalities: 13,122 PASS;
- unilateral deviations: 17,496 PASS;
- WSP equality deviations: 5,970;
- minimum positive WSP margin: `1/1000`;
- maximum allocation denominator: 12,000.

For OE, every profile allocation was independently checked to maximize a strictly positive weighted sum of its nine bundle-SD cumulative criteria over the original 22-vertex continuous fractional feasible polytope. The minimum support weight is `1/100`; support-weight denominators are at most 500. A separate continuous LP Pareto-improvement self-attack also finds no positive improvement.

## Verdict

`D8_ACCEPTABLE_SINGLETONS + {H_A}` is **CONTINUOUS SAT**.

This is a valid positive finite-domain certificate and does not depend on candidate-face completeness for its SAT direction.

It does not establish any general theorem for arbitrary n, nor does it resolve the unrestricted JET open problem.

## Next boundary target

Proceed to the other adjacent-swap pair-first boundary type:

`P_A: ab > a > empty > b`.

If `D8_ACCEPTABLE_SINGLETONS + {P_A}` is also SAT, proceed to mirror-pair extensions `{H_A,H_B}` and `{P_A,P_B}` before adding both-singletons-unacceptable types.
