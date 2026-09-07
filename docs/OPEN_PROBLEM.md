# Open problem

## Target

Determine whether ordinal efficiency (OE), envy-freeness (EF), and weak strategy-proofness (WSP) can coexist in random assignment with strict ordinal preferences over bundles.

This repository uses **bundle-level stochastic dominance**, not marginal SD.

## Canonical 3-agent, 2-good environment used for baseline work

- agents: `N={1,2,3}`;
- goods: `G={a,b}`;
- supplies: `s_a=s_b=1`;
- bundles: `{empty,a,b,ab}`;
- feasibility is fractional only; exact ex-post decomposability is not imposed.

## Methodological exclusions

No impossibility claim may be based on a bounded probability denominator, a finite candidate grid, hidden anonymity/neutrality, exact deterministic implementability, full SD-SP substituted for WSP, marginal SD substituted for bundle-level SD, a timeout treated as UNSAT, or an incomplete candidate-face library.

## Current status

**UNRESOLVED on the unrestricted domain.** Restricted-domain positive results in this repository do not settle the general question.
