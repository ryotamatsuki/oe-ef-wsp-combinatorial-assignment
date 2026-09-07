# OE–EF–WSP in Combinatorial Assignment

> **GENERAL OPEN PROBLEM: UNRESOLVED**
>
> **VERIFIED RESTRICTED-DOMAIN RESULT:** for three agents, two unit-supply goods, and the six-type domain
> \(D^\dagger=\{A,B,E,F,C,D\}\), an explicit fractional mechanism satisfies ordinal efficiency (OE),
> envy-freeness (EF), and **full bundle-level SD-strategy-proofness** (hence WSP).
>
> **INVALIDATED COMPUTATIONAL RESULT:** a historical candidate-face computation reported
> INFEASIBLE on the same six-type domain even at \(\delta=1/1000\).  That result is false because
> the explicit witness below exists.  The legacy implementation was not preserved, so its line-level
> root cause cannot currently be reconstructed.  No negative search should rely on that result.

## Research question

Can ordinal efficiency, envy-freeness, and weak strategy-proofness coexist in random assignment
with strict ordinal preferences over bundles?

The unrestricted problem remains open in this repository.  Restricted-domain existence results are
kept separate from the general claim.

## Canonical baseline

For bundles `(a,b,ab,empty)`, define

- `L = {A,E,C}` and `R = {B,F,D}`;
- `k` = number of reported L-types.

The explicit mechanism is

| k | each L-type receives | each R-type receives |
|---:|---|---|
| 0 | — | `(1/3,1/3,0,1/3)` |
| 1 | `(2/3,0,0,1/3)` | `(1/6,1/2,0,1/3)` |
| 2 | `(1/2,1/6,0,1/3)` | `(0,2/3,0,1/3)` |
| 3 | `(1/3,1/3,0,1/3)` | — |

The exact regression suite checks all 216 ordered six-type profiles, 3,888 non-trivial EF cutoff
comparisons, and 3,240 ordered unilateral deviations.

## Status summary

- Six-type explicit mechanism: **exactly verified** for feasibility, EF, and full SD-SP; OE has an
  analytic proof plus an independent continuous LP self-attack.
- Acceptable-singletons eight-type extension: **exactly verified computationally** for feasibility,
  EF, and full SD-SP on 512 ordered profiles; OE has the same analytic architecture and a continuous
  LP self-attack.  A standalone paper theorem is not yet frozen.
- Arbitrary `n`, two-good extension: **conjecture/scaffold only**; exact finite tests currently cover
  `n=2,...,10` for feasibility, EF, and full SD-SP.
- Historical six-type candidate-face INFEASIBLE: **invalidated** and archived.

## Guardrail

A future candidate-face, MILP, SMT, or CEGIS implementation must pass
`test_six_type_explicit_mechanism_is_accepted_by_solver` before it may be used for impossibility
searches.

## Run

```bash
python -m pip install -e .
python -m pip install pytest
pytest -q
```

See `docs/THEOREM_STATUS.md`, `docs/REGRESSION_AUDIT.md`, and `theory/` for the mathematical status.
