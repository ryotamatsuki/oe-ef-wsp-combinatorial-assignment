"""Exact SAT certificate for the complete 16-type frontier (n=3).

Domain: every strict ranking of {a,b,ab,empty} in which at least one singleton
is ranked above the outside option.  The mechanism is singleton PS plus a small
set of closed-form pair-upgrade rules.  Feasibility, EF and WSP are checked with
Fraction arithmetic.  OE is certified by constructing strictly positive rational
SD-support weights and checking them exactly against all 22 vertices of the
original continuous fractional feasible polytope.
"""
from fractions import Fraction as F
from functools import lru_cache

import numpy as np
from scipy.optimize import linprog

from .preferences import (
    BUNDLES,
    EIGHT_TYPE_ACCEPTABLE_SINGLETONS,
    ONE_SINGLETON_UNACCEPTABLE,
    cumulative,
)
from .boundary2_pa_certificate import vertices

RANKINGS = {**EIGHT_TYPE_ACCEPTABLE_SINGLETONS, **ONE_SINGLETON_UNACCEPTABLE}
TYPES = tuple(RANKINGS)

MIRROR = {
    "A":"B","B":"A","E":"F","F":"E","C":"D","D":"C","J":"K","K":"J",
    "H_A":"H_B","H_B":"H_A","P_A":"P_B","P_B":"P_A",
    "U_A":"U_B","U_B":"U_A","W_A":"W_B","W_B":"W_A",
}
A_SIDE = frozenset({"A","E","C","J","H_A","P_A","U_A","W_A"})
B_SIDE = frozenset(MIRROR[t] for t in A_SIDE)
S_A = frozenset({"H_A","U_A","W_A"})
S_B = frozenset({"H_B","U_B","W_B"})
Q_A = S_A | {"P_A"}
Q_B = S_B | {"P_B"}
A_ACCEPT = frozenset({"A","E","J"})

A_ROW = (F(1,3),F(0),F(0),F(2,3))
B_ROW = (F(0),F(1,3),F(0),F(2,3))
PAIR = (F(0),F(0),F(1,3),F(2,3))


def singleton_ps(profile):
    profile = tuple(profile)
    remaining = {"a": F(1), "b": F(1)}
    alloc = [{"a": F(0), "b": F(0), "empty": F(0)} for _ in profile]
    restricted = {
        t: tuple(x for x in RANKINGS[t] if x in ("a", "b", "empty"))
        for t in set(profile)
    }
    time = F(0)
    while time < 1:
        choices = []
        for t in profile:
            for obj in restricted[t]:
                if obj == "empty" or remaining[obj] > 0:
                    choices.append(obj)
                    break
        rates = {g: sum(c == g for c in choices) for g in ("a", "b")}
        event_times = [F(1) - time]
        for g in ("a", "b"):
            if rates[g]:
                event_times.append(remaining[g] / rates[g])
        dt = min(event_times)
        for i, choice in enumerate(choices):
            alloc[i][choice] += dt
        for g in ("a", "b"):
            remaining[g] -= dt * rates[g]
        time += dt
    return tuple((r["a"], r["b"], F(0), r["empty"]) for r in alloc)


def _repair_a_side(profile):
    p = tuple(profile)
    # All reports are b-unacceptable and at least one is pair-first P_A.
    if all(t in Q_A for t in p) and "P_A" in p:
        return tuple(PAIR if t == "P_A" else A_ROW for t in p)

    qs = [t for t in p if t in Q_A]
    others = [t for t in p if t not in Q_A]
    if len(qs) != 2 or len(others) != 1:
        return None
    x = others[0]
    n_p = sum(t == "P_A" for t in qs)

    # One ordinary a-oriented acceptable type plus two b-unacceptable types.
    if x in A_ACCEPT and n_p >= 1:
        bshare = F(1) - F(n_p, 3)
        xrow = (F(1,3), bshare, F(0), F(1) - F(1,3) - bshare)
        return tuple(PAIR if t == "P_A" else A_ROW if t in S_A else xrow for t in p)

    # C is pair-first and can absorb residual b capacity through ab.
    if x == "C":
        bshare = F(1) - F(1 + n_p, 3)
        xrow = (F(0), bshare, F(1,3), F(1) - bshare - F(1,3))
        return tuple(PAIR if t == "P_A" else A_ROW if t in S_A else xrow for t in p)
    return None


def _swap_row(row):
    return (row[1], row[0], row[2], row[3])


def mechanism(profile):
    """Closed-form OE+EF+WSP mechanism on the complete 16-type frontier."""
    p = tuple(profile)

    # P_B plus two A-oriented unacceptable reports; m=#P_A among the other two.
    if p.count("P_B") == 1 and sum(t in Q_A for t in p) == 2:
        m = sum(t == "P_A" for t in p)
        pb = (F(0), F(2-m,3), F(1,3), F(m,3))
        return tuple(pb if t == "P_B" else PAIR if t == "P_A" else A_ROW for t in p)

    # Exact mirror of the preceding rule.
    if p.count("P_A") == 1 and sum(t in Q_B for t in p) == 2:
        m = sum(t == "P_B" for t in p)
        pa = (F(2-m,3), F(0), F(1,3), F(m,3))
        return tuple(pa if t == "P_A" else PAIR if t == "P_B" else B_ROW for t in p)

    # C plus two B-oriented unacceptable reports; m=#P_B.
    if p.count("C") == 1 and sum(t in Q_B for t in p) == 2:
        m = sum(t == "P_B" for t in p)
        crow = (F(2-m,3), F(0), F(1,3), F(m,3))
        return tuple(crow if t == "C" else PAIR if t == "P_B" else B_ROW for t in p)

    # Exact mirror: D plus two A-oriented unacceptable reports.
    if p.count("D") == 1 and sum(t in Q_A for t in p) == 2:
        m = sum(t == "P_A" for t in p)
        drow = (F(0), F(2-m,3), F(1,3), F(m,3))
        return tuple(drow if t == "D" else PAIR if t == "P_A" else A_ROW for t in p)

    # Pure A-side repair.
    r = _repair_a_side(p)
    if r is not None:
        return r

    # Pure B-side mirror repair.
    if all(t in B_SIDE for t in p):
        ap = tuple(MIRROR[t] for t in p)
        ar = _repair_a_side(ap)
        if ar is not None:
            return tuple(_swap_row(row) for row in ar)

    return singleton_ps(p)


def _vertex_allocation(v):
    rows = []
    for i in range(3):
        a, b, ab = v[3*i:3*i+3]
        rows.append((a, b, ab, F(1) - a - b - ab))
    return tuple(rows)


def _criteria(profile, allocation):
    vals = []
    for i, t in enumerate(profile):
        vals.extend(cumulative(allocation[i], RANKINGS[t]))
    return tuple(vals)


@lru_cache(maxsize=None)
def support_weights(profile):
    """Construct and exactly validate strictly positive SD-support weights.

    HiGHS is used only to locate a rational witness.  The returned Fraction vector
    is then checked exactly against all 22 vertices, so numerical optimality is not
    accepted as the certificate.
    """
    profile = tuple(profile)
    target = _criteria(profile, mechanism(profile))
    diffs = []
    for v in vertices():
        other = _criteria(profile, _vertex_allocation(v))
        diffs.append(tuple(x - y for x, y in zip(target, other)))

    # variables: nine weights and common lower bound t; maximize t.
    a_ub, b_ub = [], []
    for d in diffs:
        a_ub.append([-float(x) for x in d] + [0.0])
        b_ub.append(0.0)
    for j in range(9):
        row = [0.0] * 10
        row[j] = -1.0
        row[9] = 1.0
        a_ub.append(row)
        b_ub.append(0.0)

    result = linprog(
        [0.0] * 9 + [-1.0],
        A_ub=np.asarray(a_ub), b_ub=np.asarray(b_ub),
        A_eq=np.asarray([[1.0] * 9 + [0.0]]), b_eq=np.asarray([1.0]),
        bounds=[(0, None)] * 10,
        method="highs",
    )
    if not result.success or result.x[9] <= 1e-10:
        raise AssertionError(f"No positive support located for {profile}")

    w = [F(float(x)).limit_denominator(100000) for x in result.x[:9]]
    total = sum(w)
    w = tuple(x / total for x in w)
    if min(w) <= 0:
        raise AssertionError(f"Non-positive rationalized support for {profile}")

    for d in diffs:
        if sum(w[k] * d[k] for k in range(9)) < 0:
            raise AssertionError(f"Rationalized support fails exactly for {profile}")
    return w


def verify_supported_oe(profile):
    w = support_weights(tuple(profile))
    return len(w) == 9 and min(w) > 0
