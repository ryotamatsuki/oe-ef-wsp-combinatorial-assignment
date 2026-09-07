# Arbitrary-n, two-good acceptable-singletons theorem

**Status: ANALYTICALLY CLOSED / FROZEN POSITIVE THEOREM.**

## Theorem

Let `n>=2`. There are two unit-supply goods `a,b` and bundles `{a,b,ab,empty}`. Each agent has a strict ranking satisfying

`a > empty` and `b > empty`.

Equivalently, with four bundles this is the eight-ranking domain `D8_ACCEPTABLE_SINGLETONS`.

Then there exists a fractional mechanism satisfying:

- feasibility;
- ordinal efficiency (OE) with respect to the full continuous fractional feasible set;
- envy-freeness (EF) under bundle-level stochastic dominance;
- full bundle-level SD-strategy-proofness, hence WSP.

No anonymity, neutrality, deterministic decomposability, denominator restriction, or candidate-face restriction is assumed as an axiom. The constructed mechanism itself is symmetric.

## Closed-form mechanism

Classify an agent as `L` when `a>b` and `R` when `b>a`. Let `k` be the number of L-agents and let

`h=2/n`, `z=1-2/n`.

Every agent receives zero probability of `ab`, total singleton probability `h`, and outside probability `z`.

The singleton probabilities are:

- `k=0` or `k=n`: every agent gets `(p,q)=(1/n,1/n)`;
- `0<2k<n`: every L gets `(h,0)`; every R gets `(h-1/(n-k), 1/(n-k))`;
- `2k=n`: every L gets `(h,0)`; every R gets `(0,h)`;
- `n<2k<2n`: every L gets `(1/k, h-1/k)`; every R gets `(0,h)`.

Thus each row is `(p,q,0,z)`.

This is the two-singleton eating allocation, written in closed form.

## 1. Feasibility

Row sums are one by construction and `z>=0` because `n>=2`.

If `0<2k<n`, then

`sum_i q_i=(n-k)/(n-k)=1`,

and

`sum_i p_i=k(2/n)+(n-k)(2/n-1/(n-k))=2-1=1`.

Nonnegativity of the R cross-share follows from `2k<n`, which gives `2/n>1/(n-k)`.

The case `2k>n` is the mirror image. If `2k=n`, each capacity is exactly one. At `k=0,n`, each capacity is `n(1/n)=1`.

Hence both good capacities bind at every profile.

## 2. Envy-freeness

At every allocation produced by the rule,

`r_i=0`, `p_i+q_i=h`, and `z_i=z`

for all agents.

For an L-type, the four possible rankings in the acceptable-singletons domain generate nontrivial cumulative vectors of the forms

- `(0,p,h)`;
- `(p,p,h)`;
- `(p,h,h)`;
- `(p,h,1)`.

Therefore, holding `h,r,z` fixed, every bundle-SD cutoff is weakly increasing in `p` and otherwise constant. Thus an L-agent does not envy another row whenever its own `p` is weakly largest. Symmetrically, an R-agent only needs its own `q` to be weakly largest.

The closed-form rule has exactly this property:

- if `2k<n`, L-agents have `p=h` while R-agents have `p<h`, and R-agents have `q=1/(n-k)>0` while L-agents have `q=0`;
- if `2k>n`, the mirror statement holds;
- if `2k=n`, each group receives its preferred singleton with probability `h` and the other group receives zero of it;
- if `k=0` or `k=n`, all rows coincide.

Hence the mechanism is EF under bundle-level SD.

## 3. Full SD-strategy-proofness

A report change within the same L/R class leaves `k`, every row, and therefore the entire allocation unchanged.

Consider an L-agent whose truthful profile has `k>=1` L-agents. Its truthful probability of `a` is

`p^T=min{2/n,1/k}`.

If it reports an R-type, the total number of L-reports becomes `k-1`. The deviator's resulting a-probability is

`p^M=max{0, 2/n - 1/(n-k+1)}`.

If `p^T=2/n`, then `p^T>=p^M` immediately. Otherwise `p^T=1/k`. If `p^M>0`, then

`1/k + 1/(n-k+1) >= 4/(n+1) > 2/n`

for every `n>=2`, because the two denominators sum to `n+1`. Hence `1/k>2/n-1/(n-k+1)=p^M`.

Thus an L-agent never increases its preferred-singleton probability by crossing to R.

The R-to-L case is symmetric: with `k` truthful L-reports,

`q^T=min{2/n,1/(n-k)}`

and after an R-agent crosses to L,

`q^M=max{0,2/n-1/(k+1)}`,

with the same reciprocal inequality implying `q^T>=q^M`.

Because `h,r,z` are profile-independent constants and every true L-ranking's cumulative vector is monotone only in `p` (and every true R-ranking's only in `q`), these inequalities imply truthful allocation weakly SD-dominates every misreport allocation. Cross-class deviations are in fact strictly worse at some cutoff; within-class deviations are exact equality.

Therefore the mechanism is full bundle-level SD-strategy-proof.

## 4. Ordinal efficiency

Fix a profile and let `x` be the mechanism allocation. Suppose a feasible allocation `y` weakly SD-dominates `x` for every agent.

Write

`h_i(y)=y_i(a)+y_i(b)+y_i(ab)`.

For the two rankings with `empty` above `ab`, namely `A` and `B`, the third cutoff of `x` equals one. Hence SD dominance forces `y_i(ab)=0`; their second cutoff then implies `h_i(y)>=2/n`.

For every other ranking in `D8_ACCEPTABLE_SINGLETONS`, `empty` is last, so the third cutoff directly implies `h_i(y)>=2/n`.

Thus for every agent,

`h_i(y)>=2/n`.

Adding the two capacity constraints yields

`2 >= sum_i[y_i(a)+y_i(b)+2y_i(ab)]`

`   = sum_i h_i(y) + sum_i y_i(ab)`

`   >= 2 + sum_i y_i(ab)`.

Therefore

`y_i(ab)=0` and `h_i(y)=2/n`

for every agent. Consequently outside probability is also fixed at `1-2/n`. Any remaining weak SD improvement can only reallocate singleton probability.

For an L-agent, weak SD dominance now requires

`y_i(a)>=x_i(a)`;

for an R-agent it requires

`y_i(b)>=x_i(b)`.

Both singleton capacities must bind under `y`, because total singleton mass is exactly `n(2/n)=2` and each capacity is at most one.

If `2k<n`, every L-agent already has `x_i(a)=2/n`, the maximum compatible with its fixed row sum. Hence no L-agent can strictly improve. Since total a- and b-capacities remain fixed, no R-agent can strictly improve either.

If `2k>n`, every R-agent already has `x_i(b)=2/n`, so the mirror argument applies.

If `2k=n`, both groups already receive their preferred singleton with probability `2/n` and no strict improvement is possible.

If `k=0` or `k=n`, all agents belong to one group; their preferred-good capacity already sums to one, so coordinatewise weak improvement with one strict inequality is impossible.

Hence no feasible allocation weakly SD-improves everyone and strictly improves someone. The mechanism is OE with respect to the original continuous fractional feasible set.

## Consequence

For every `n>=2`, the acceptable-singletons domain admits an OE + EF + full SD-SP mechanism. In particular, the earlier three-agent eight-type computational extension is subsumed by this theorem.

This theorem is a boundary result, not a solution of the unrestricted bundle-preference open problem. It does not apply once at least one singleton is ranked below the outside option.
