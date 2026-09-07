# Computational history

## Valid baseline

Astra Round 1 produced an explicit six-type rule. Its existence proof does not depend on solver output. The repository regression suite independently checks the finite EF and incentive constraints with `fractions.Fraction`.

## Invalidated lead

A previous ephemeral candidate-face calculation reported INFEASIBLE on `D†={A,B,E,F,C,D}` even with WSP margin `delta=1/1000`.

This cannot be a valid statement about the mathematical model: the explicit mechanism has cross-group truthful SD advantage `1/3` and exact equality for same-group reports.

The old source/model files were not preserved in the newly created repository or available conversation/library artifacts. Therefore a line-level forensic root cause cannot be asserted. The failure is archived as an invalidated result rather than silently deleted.

## Regression policy

Before any future impossibility search:
1. exact six-type witness tests must pass;
2. the solver must accept the known-good witness;
3. any candidate-face representation must demonstrate that the witness belongs to an admissible OE face for every profile;
4. `D8_ACCEPTABLE_SINGLETONS` and `D8_OUTSIDE_OPTION_CROSSING` must remain distinct.
