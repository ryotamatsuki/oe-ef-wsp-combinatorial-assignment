# Arbitrary-n, two-good extension — scaffold only

**Status: conjecture / proof scaffold, not a frozen theorem.**

Assume `n>=2`, two unit-supply goods `a,b`, and every admissible strict ranking satisfies `a>empty` and `b>empty`.

Classify an agent as L if `a>b`, R otherwise. Let `k` be the number of L-agents.

Candidate rule:
- every agent receives total nonempty probability `2/n`;
- no agent receives `ab`;
- singleton probabilities are the two-object probabilistic-serial allocation.

Explicitly:
- if `k=0` or `k=n`, every agent receives `1/n` of each singleton;
- if `2k<n`, each L receives `2/n` of a; each R receives `1/(n-k)` of b and `2/n-1/(n-k)` of a;
- if `2k>n`, each R receives `2/n` of b; each L receives `1/k` of a and `2/n-1/k` of b;
- if `2k=n`, L receives `2/n` of a and R receives `2/n` of b;
- every row has outside probability `1-2/n`.

`tests/test_arbitrary_n_scaffold.py` verifies with exact rational arithmetic feasibility, EF, and full SD-SP for all binary L/R profiles and all compatible eight-type true preferences for `n=2,...,10`.

No general theorem is claimed until the analytic OE and incentive proof is separately frozen.
