# OE–EF–WSP in Combinatorial Assignment

> **GENERAL OPEN PROBLEM: UNRESOLVED**
>
> **VERIFIED POSITIVE BOUNDARY THEOREM:** for every `n>=2`, two unit-supply goods, and every strict bundle ranking satisfying `a>empty` and `b>empty`, an explicit fractional mechanism satisfies ordinal efficiency (OE), envy-freeness (EF), and **full bundle-level SD-strategy-proofness** (hence WSP).
>
> **VERIFIED COMPLETE 16-TYPE FRONTIER SAT (n=3):** when the domain contains **every** strict ranking for which at least one singleton is above the outside option, an explicit fractional mechanism satisfies OE+EF+WSP on all 4,096 ordered profiles.
>
> **INVALIDATED COMPUTATIONAL RESULT:** a historical candidate-face computation reported INFEASIBLE on the six-type domain even at `delta=1/1000`. That result is false because an explicit witness exists. The legacy implementation was not preserved, so its line-level root cause cannot currently be reconstructed.

## Research question

Can ordinal efficiency, envy-freeness, and weak strategy-proofness coexist in random assignment with strict ordinal preferences over bundles?

The unrestricted problem remains open. The positive theorem and finite-domain certificates below map a verified possibility frontier; they do not solve the unrestricted problem.

## Arbitrary-n positive theorem

For bundles `(a,b,ab,empty)`, assume every admissible strict ranking satisfies

- `a > empty`, and
- `b > empty`.

The closed-form rule in `theory/arbitrary_n_two_goods.md` is analytically proved, for every `n>=2`, to be feasible, OE against the original continuous fractional feasible set, EF, and full bundle-level SD-strategy-proof.

## Complete n=3 positive frontier

For three agents, the positive region extends strictly beyond the arbitrary-n theorem. Define

`D16_ONE_SINGLETON_ACCEPTABLE`

as all 16 strict rankings in which at least one singleton is above the outside option.

The mechanism in `src/boundary16_certificate.py` satisfies:

- 4,096 ordered profiles;
- 73,728 non-trivial EF cutoff inequalities: exact PASS;
- 184,320 ordered unilateral deviations: exact WSP PASS;
- 44,400 WSP equality deviations;
- minimum positive WSP margin `1/6`;
- maximum allocation denominator 6;
- continuous OE certified against the exact 22-vertex feasible polytope with strictly positive rational SD-support weights.

See `docs/BOUNDARY_ATTACK_D16_RESULT.md`.

## Current frontier

The one-singleton-unacceptable region is now completely SAT for `n=3,m=2`. The next negative-search domain adds types with **both** singletons below the outside option, beginning with

- `T_A: ab > empty > a > b`;
- `T_B: ab > empty > b > a`.

The next target is

`D18_T_MIRROR = D16_ONE_SINGLETON_ACCEPTABLE + {T_A,T_B}`.

See `docs/BOUNDARY_SEARCH_PLAN.md`.

## Regression guardrail

A future candidate-face, MILP, SMT, or CEGIS implementation must pass `test_six_type_explicit_mechanism_is_accepted_by_solver` before it may be used for impossibility searches. Passing that fixture prevents a known false negative; it does not by itself prove solver completeness on new preference domains.

## Run

```bash
python -m pip install -e .
python -m pip install pytest
pytest -q
```

See `docs/THEOREM_STATUS.md`, `docs/REGRESSION_AUDIT.md`, and `theory/` for the mathematical status.
