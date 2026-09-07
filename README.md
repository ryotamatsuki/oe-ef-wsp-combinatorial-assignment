# OE–EF–WSP in Combinatorial Assignment

> **GENERAL OPEN PROBLEM: UNRESOLVED**
>
> **VERIFIED POSITIVE BOUNDARY THEOREM:** for every `n>=2`, two unit-supply goods, and every strict bundle ranking satisfying `a>empty` and `b>empty`, an explicit fractional mechanism satisfies ordinal efficiency (OE), envy-freeness (EF), and **full bundle-level SD-strategy-proofness** (hence WSP).
>
> **INVALIDATED COMPUTATIONAL RESULT:** a historical candidate-face computation reported INFEASIBLE on the six-type domain even at `delta=1/1000`. That result is false because an explicit witness exists. The legacy implementation was not preserved, so its line-level root cause cannot currently be reconstructed.

## Research question

Can ordinal efficiency, envy-freeness, and weak strategy-proofness coexist in random assignment with strict ordinal preferences over bundles?

The unrestricted problem remains open. The positive theorem below identifies a restricted-domain boundary; it does not solve the unrestricted problem.

## Positive theorem

For bundles `(a,b,ab,empty)`, assume every admissible strict ranking satisfies

- `a > empty`, and
- `b > empty`.

Classify a report as L if `a>b` and R if `b>a`. Let `k` be the number of L-reports and let `h=2/n`.

The closed-form rule gives every agent:

- zero probability of `ab`;
- total singleton probability `h`;
- outside probability `1-h`;
- the two-singleton eating allocation determined by `k`.

`theory/arbitrary_n_two_goods.md` proves analytically, for every `n>=2`, that this rule is feasible, OE against the original continuous fractional feasible set, EF, and full bundle-level SD-strategy-proof.

The earlier three-agent six-type and eight-type acceptable-singletons results are special cases/corollaries of this architecture.

## Boundary for the next search

The theorem stops applying as soon as at least one singleton is ranked below the outside option. Negative-search work therefore starts with **one-singleton-unacceptable** types before moving to types where both singletons are unacceptable.

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
