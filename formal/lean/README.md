# Lean formal verification

This directory is the machine-checked companion for the OE–EF–WSP combinatorial-assignment project.

## Current certified scope

The bootstrap formalization covers the canonical six-type theorem `D†={A,B,E,F,C,D}` for `n=3`, using exact rational arithmetic:

- fractional feasibility of the explicit mechanism on all 216 ordered profiles;
- bundle-level envy-freeness on all 216 ordered profiles;
- full bundle-level SD-strategy-proofness for every agent, profile, and report in the six-type domain.

The Lean definitions mirror the canonical Python definitions in `src/preferences.py` and `src/mechanism_six_type.py`.

## Not yet Lean-certified

Ordinal efficiency against the full continuous fractional feasible set is **not** claimed as Lean-certified in this bootstrap. The repository's current OE authority remains the analytic proof in `theory/six_type_explicit_mechanism.md` plus the existing independent computational self-attack. A later formalization should model arbitrary real-valued feasible outcomes and prove the continuous OE argument directly.

The unrestricted OE+EF+WSP open problem is unchanged.

## Files

- `OEEFWSP/Basic.lean` — bundles, exact rational lottery rows, outcomes, and feasibility.
- `OEEFWSP/SixType.lean` — six types, rankings, SD cutoffs, explicit mechanism, EF, and full SD-SP theorems.
- `OEEFWSP.lean` — library root.
- `CROSSWALK.md` — manuscript/code-to-Lean authority map.
- `lean-toolchain` — pinned Lean version.
- `lakefile.toml` — pinned Mathlib dependency.

## Reproduce locally or in Codespaces

From this directory:

```bash
lake update
lake build --wfail
```

The GitHub Actions workflow `.github/workflows/lean.yml` runs the same formal build on pushes and pull requests that touch this directory.

## Trust discipline

A green Lean build means the stated Lean declarations type-check under the pinned Lean/Mathlib environment. It does **not** by itself establish that the Lean statement is the economically intended theorem. That correspondence is controlled by `CROSSWALK.md` and should be audited whenever the manuscript, Python canonical definitions, or Lean statements change.
