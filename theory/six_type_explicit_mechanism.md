# Six-type explicit mechanism

Let `L={A,E,C}`, `R={B,F,D}`, and let `k` be the number of L-reports. Write `x_i=(p_i,q_i,r_i,z_i)=(x_i(a),x_i(b),x_i(ab),x_i(empty))`.

| k | L row | R row |
|---:|---|---|
| 0 | — | `(1/3,1/3,0,1/3)` |
| 1 | `(2/3,0,0,1/3)` | `(1/6,1/2,0,1/3)` |
| 2 | `(1/2,1/6,0,1/3)` | `(0,2/3,0,1/3)` |
| 3 | `(1/3,1/3,0,1/3)` | — |

Thus `r_i=0`, `z_i=1/3`, and `p_i+q_i=2/3` for every agent.

## Feasibility

Each row sums to one and in every case `sum_i p_i=sum_i q_i=1`, `sum_i r_i=0`.

## Envy-freeness

At the explicit allocation, the nontrivial cumulative vectors are:

- A: `(p,2/3,1)`
- B: `(q,2/3,1)`
- E: `(p,p,2/3)`
- F: `(q,q,2/3)`
- C: `(0,p,2/3)`
- D: `(0,q,2/3)`

Hence an L-type only needs its own `p` to be weakly largest and an R-type its own `q`; the table has this property for all `k`.

## Full SD-strategy-proofness

Within L or within R, a report change leaves the entire allocation unchanged. Across groups, the probability of the true type's preferred singleton falls by exactly `1/3` under the misreport, while total nonempty probability stays `2/3` and `ab` remains zero. The truth-minus-misreport cumulative differences are `(1/3,0,0)` for A/B, `(1/3,1/3,0)` for E/F, and `(0,1/3,0)` for C/D. Hence truth weakly SD-dominates every misreport.

## Ordinal efficiency

Suppose feasible `y` weakly SD-dominates the rule's allocation `x` for every agent. Let `h_i(y)=y_i(a)+y_i(b)+y_i(ab)`.

For A/B, the third cutoff of `x` is one, so dominance requires `y_i(ab)=0`, and the second cutoff implies `h_i(y)>=2/3`. For E/F/C/D the third cutoff gives `h_i(y)>=2/3`.

Capacity implies

`2 >= sum_i[y_i(a)+y_i(b)+2y_i(ab)] = sum_i h_i(y)+sum_i y_i(ab) >= 2+sum_i y_i(ab)`.

Therefore `y_i(ab)=0` and `h_i(y)=2/3` for every agent. Only singleton reallocations remain. For `k=1`, the unique L-agent must keep a-probability at least `2/3`, fixing its row; each R-agent must keep b-probability at least `1/2`, and b-capacity fixes both. `k=2` is the mirror. At `k=0`, every R-agent needs at least `1/3` of b; at `k=3`, every L-agent needs at least `1/3` of a. Hence `y=x` in every case, so no strict SD-Pareto improvement exists.
