# Candidate-face regression audit

## Historical failure

Reported result: `D†={A,B,E,F,C,D}`, `delta=1/1000` -> INFEASIBLE.

Status: **INVALIDATED**.

## Golden witness audit

The explicit mechanism passes the mathematical constraints directly:

- feasibility: PASS on all 216 profiles;
- EF: PASS on all 3,888 non-trivial cutoff comparisons;
- full SD-SP: PASS on all 3,240 ordered deviations;
- WSP: follows immediately;
- OE: analytic proof over all fractional feasible comparison allocations.

For cross-group deviations the truthful cumulative vector has a `1/3` strict advantage at one or more relevant cutoffs. For same-group deviations the allocation is exactly unchanged. Hence a correct WSP branch formulation with `delta=1/1000` must admit the witness.

## First-failing-constraint report

A literal first failing legacy constraint cannot be produced because the historical solver source, candidate-face library, and generated constraint matrix were not persisted.

```text
profile: not recoverable from legacy artifact
agent: not recoverable
true type: not recoverable
misreport type if relevant: not recoverable
allocation: explicit Astra witness passes all mathematical constraints
constraint family: legacy implementation-only
expected mathematical inequality: satisfied
encoded inequality: unavailable
left-hand side: unavailable
right-hand side: unavailable
reason for discrepancy: historical implementation/model artifact not preserved
root cause: unresolved at line level
```

## Strongest localization justified by evidence

Candidate-face completeness is the highest-priority suspect because the witness is OE even with `ab=0` for pair-first C/D types, including the legal endpoint `t=0` at `(C,C,C)` and `(D,D,D)`. This is a hypothesis, not a forensic finding; profile mapping, branch encoding, or other implementation errors remain possible without the lost code.

## Permanent fix

The repository now contains a hard regression gate: `test_six_type_explicit_mechanism_is_accepted_by_solver`. Future generic solver code must be integrated behind that gate. A solver that rejects the witness is not authorized for negative-search results.
