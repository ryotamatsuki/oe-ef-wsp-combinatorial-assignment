"""OE verification.

The analytic theorem is canonical. The LP routine is an independent numerical self-attack
against the original continuous fractional feasibility set.
"""

import numpy as np
from scipy.optimize import linprog
from .preferences import BUNDLES, cumulative

INDEX = {b: i for i, b in enumerate(BUNDLES)}


def six_type_analytic_oe(allocation, profile):
    """Verify the Astra OE characterization for the six-type domain."""
    left = {"A", "E", "C"}
    for row, t in zip(allocation, profile):
        if t in {"A", "B", "E", "F"} and row[2] != 0:
            return False
    if sum(r[0] + r[2] for r in allocation) != 1:
        return False
    if sum(r[1] + r[2] for r in allocation) != 1:
        return False
    l_b = sum(row[1] for row, t in zip(allocation, profile) if t in left)
    r_a = sum(row[0] for row, t in zip(allocation, profile) if t not in left)
    return l_b == 0 or r_a == 0


def lp_sd_improvement_gain(profile, allocation, rankings):
    n = len(profile)
    dim = 4 * n
    a_eq, b_eq = [], []
    for i in range(n):
        row = np.zeros(dim)
        row[4*i:4*i+4] = 1
        a_eq.append(row)
        b_eq.append(1.0)

    a_ub, b_ub = [], []
    for good in (0, 1):
        row = np.zeros(dim)
        for i in range(n):
            row[4*i + good] = 1
            row[4*i + 2] = 1
        a_ub.append(row)
        b_ub.append(1.0)

    score = np.zeros(dim)
    baseline = 0.0
    for i, t in enumerate(profile):
        base = cumulative(allocation[i], rankings[t])
        for cutoff in range(1, 4):
            row = np.zeros(dim)
            for bundle in rankings[t][:cutoff]:
                row[4*i + INDEX[bundle]] = 1
            a_ub.append(-row)
            b_ub.append(-float(base[cutoff-1]))
            score += row
            baseline += float(base[cutoff-1])

    result = linprog(
        -score,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=np.asarray(a_eq),
        b_eq=np.asarray(b_eq),
        bounds=(0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return -result.fun - baseline
