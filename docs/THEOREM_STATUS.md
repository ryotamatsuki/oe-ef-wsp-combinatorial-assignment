# Theorem status

## T1 — Six-type explicit existence theorem

**Status: VERIFIED RESTRICTED-DOMAIN THEOREM.**

Domain `D†={A,B,E,F,C,D}` with full strict rankings as defined in `src/preferences.py`.
For three agents and two unit-supply goods, the explicit rule in `theory/six_type_explicit_mechanism.md` satisfies fractional feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

Evidence:
- exact rational checks of all 216 profiles;
- exact rational checks of all 3,888 non-trivial EF cutoff inequalities;
- exact rational checks of all 3,240 ordered unilateral deviations;
- analytic OE proof over the full continuous fractional feasible set;
- numerical LP self-attack over the original continuous feasible set as corroboration only.

## T2 — Acceptable-singletons eight-type extension

**Status: VERIFIED COMPUTATIONAL EXTENSION; ANALYTIC FREEZE PENDING.**

Add `J: a>b>ab>empty` and `K: b>a>ab>empty`. The same explicit mechanism passes exact feasibility, EF, and full SD-SP checks on all `8^3=512` profiles and all 10,752 ordered deviations. Continuous OE LP self-attack finds no positive improvement within numerical tolerance.

## C1 — Arbitrary-n, two-good acceptable-singletons extension

**Status: CONJECTURE / SCAFFOLD.**

Candidate: total nonempty probability `2/n`, no `ab`, singleton allocation determined only by whether the report has `a>b` or `b>a`. Exact finite tests cover `n=2,...,10` for feasibility, EF, and full SD-SP. No general theorem is claimed here.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
