# OE–EF–WSP in Combinatorial Assignment

> **GENERAL OPEN PROBLEM: UNRESOLVED**
>
> **VERIFIED POSITIVE BOUNDARY THEOREM:** for every `n>=2`, two unit-supply goods, and every strict bundle ranking satisfying `a>empty` and `b>empty`, an explicit fractional mechanism satisfies ordinal efficiency (OE), envy-freeness (EF), and **full bundle-level SD-strategy-proofness** (hence WSP).
>
> **VERIFIED ONE-SIDED BOUNDARY SAT:** for three agents, both minimal adjacent-swap extensions `D_acc+{H_A}` and `D_acc+{P_A}` admit exact OE+EF+WSP mechanisms. A single one-direction outside-option crossing is therefore not an impossibility core.
>
> **INVALIDATED COMPUTATIONAL RESULT:** a historical candidate-face computation reported INFEASIBLE on the six-type domain even at `delta=1/1000`. That result is false because an explicit witness exists. The legacy implementation was not preserved, so its line-level root cause cannot currently be reconstructed.

## Research question

Can ordinal efficiency, envy-freeness, and weak strategy-proofness coexist in random assignment with strict ordinal preferences over bundles?

The unrestricted problem remains open. The positive theorem and finite-domain certificates below map a verified possibility frontier; they do not solve the unrestricted problem.

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

## Current boundary map for n=3

Two minimal one-singleton-unacceptable adjacent-swap types have now been closed positively:

- `H_A: a > ab > empty > b` — exact finite-domain SAT certificate;
- `P_A: ab > a > empty > b` — exact finite-domain SAT certificate.

For `P_A`, singleton PS already satisfies feasibility, EF, and WSP on all 729 profiles; only 13 profiles require a closed-form OE repair. The final exact mechanism has maximum allocation denominator 6 and minimum positive WSP margin `1/6`. OE is certified by exact enumeration of the 22 vertices of the original continuous feasible polytope and strictly positive rational SD-support weights with denominator at most 15.

The next target is **two-sided outside-option crossing**:

`D8_ACCEPTABLE_SINGLETONS + {H_A,H_B}`.

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
