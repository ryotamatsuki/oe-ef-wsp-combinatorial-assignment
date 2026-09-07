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

## T2 — Arbitrary-n, two-good acceptable-singletons existence theorem

**Status: ANALYTICALLY CLOSED / FROZEN POSITIVE THEOREM.**

For every `n>=2`, two unit-supply goods `a,b`, and the full strict-ranking domain satisfying

`a > empty` and `b > empty`,

there exists an explicit fractional mechanism satisfying feasibility, OE, EF, and full bundle-level SD-strategy-proofness.

The rule gives every agent total nonempty probability `2/n`, zero probability of `ab`, outside probability `1-2/n`, and uses a closed-form two-singleton eating allocation based only on whether the report has `a>b` or `b>a`.

The proof in `theory/arbitrary_n_two_goods.md` is fully analytic:
- feasibility is checked in all `k=#L` regimes;
- bundle-level EF follows from the complete cumulative-cutoff forms;
- full SD-SP follows from direct cross-class report inequalities;
- OE is proved against the original continuous fractional feasible set, not a candidate face or grid.

The earlier three-agent eight-type acceptable-singletons result is a corollary of T2 and no longer has a separate pending analytic status.

## Boundary implication

T2 identifies a precise applicability boundary: the proof requires both singletons to be ranked above the outside option. It does **not** cover any type with `empty > a` or `empty > b`.

The next search therefore begins with minimal one-singleton-unacceptable extensions before adding types with both singletons unacceptable.

## Invalidated result

The historical claim that the six-type candidate-face model is INFEASIBLE at `delta=1/1000` is **INVALIDATED** because T1 supplies an explicit witness.
