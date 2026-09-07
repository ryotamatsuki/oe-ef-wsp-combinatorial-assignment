"""Exact certificate for D8_ACCEPTABLE_SINGLETONS + {P_A}.

P_A: ab > a > empty > b.

The mechanism is singleton PS except at the 13 profiles with at least two P_A
reports where singleton PS is not ordinally efficient.  OE is certified without
a numerical LP: the original 9-dimensional feasible polytope is vertex-enumerated
exactly from its 14 facets, and a strictly positive rational SD scalarization with
denominator at most 15 is found by finite composition search at every profile.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations

from .preferences import BUNDLES, EIGHT_TYPE_ACCEPTABLE_SINGLETONS, ONE_SINGLETON_UNACCEPTABLE, cumulative

RANKINGS = {
    **EIGHT_TYPE_ACCEPTABLE_SINGLETONS,
    "P_A": ONE_SINGLETON_UNACCEPTABLE["P_A"],
}
TYPES = tuple(RANKINGS)


def _singleton_ps(profile):
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


_PAIR_ROW = (F(0), F(0), F(1, 3), F(2, 3))
_MIXED_ROW = (F(1, 3), F(1, 3), F(0), F(1, 3))


def mechanism(profile):
    """Exact OE+EF+WSP mechanism on the 9-type P_A boundary domain."""
    profile = tuple(profile)
    count_p = profile.count("P_A")
    if count_p == 3:
        return (_PAIR_ROW, _PAIR_ROW, _PAIR_ROW)
    if count_p == 2:
        non_p = [t for t in profile if t != "P_A"]
        if len(non_p) == 1 and non_p[0] in {"A", "E", "J", "C"}:
            other = non_p[0]
            out = []
            for t in profile:
                if t == "P_A":
                    out.append(_PAIR_ROW)
                elif other == "C":
                    out.append(_PAIR_ROW)
                else:
                    out.append(_MIXED_ROW)
            return tuple(out)
    return _singleton_ps(profile)


# Base feasible polytope in nonempty variables [a,b,ab] for three agents.
def _facets():
    A, b = [], []
    for j in range(9):
        row = [0] * 9
        row[j] = -1
        A.append(tuple(row)); b.append(0)
    for i in range(3):
        row = [0] * 9
        row[3*i:3*i+3] = [1, 1, 1]
        A.append(tuple(row)); b.append(1)
    row = [0] * 9
    for i in range(3):
        row[3*i] = 1; row[3*i+2] = 1
    A.append(tuple(row)); b.append(1)
    row = [0] * 9
    for i in range(3):
        row[3*i+1] = 1; row[3*i+2] = 1
    A.append(tuple(row)); b.append(1)
    return tuple(A), tuple(b)


def _solve_square(rows, rhs):
    n = len(rhs)
    M = [[F(rows[i][j]) for j in range(n)] + [F(rhs[i])] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col] != 0), None)
        if pivot is None:
            return None
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r == col:
                continue
            factor = M[r][col]
            if factor:
                M[r] = [M[r][j] - factor * M[col][j] for j in range(n + 1)]
    return tuple(M[i][-1] for i in range(n))


@lru_cache(maxsize=1)
def vertices():
    """Enumerate the complete 22-vertex continuous feasible polytope exactly."""
    A, b = _facets()
    out = set()
    for active in combinations(range(14), 9):
        sol = _solve_square([A[i] for i in active], [b[i] for i in active])
        if sol is None:
            continue
        if all(sum(F(row[j]) * sol[j] for j in range(9)) <= F(rhs)
               for row, rhs in zip(A, b)):
            out.add(sol)
    assert len(out) == 22
    return tuple(sorted(out))


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


def _positive_compositions(total, parts=9):
    for cuts in combinations(range(1, total), parts - 1):
        prev = 0
        values = []
        for cut in cuts + (total,):
            values.append(cut - prev)
            prev = cut
        yield tuple(values)


@lru_cache(maxsize=None)
def support_weights(profile):
    """Return exact strictly positive SD weights supporting mechanism(profile).

    Denominators 9,...,15 are searched exhaustively.  The comparison is exact
    against every vertex, hence support establishes OE on the whole continuous
    fractional feasible polytope.
    """
    profile = tuple(profile)
    target = _criteria(profile, mechanism(profile))
    diffs = []
    for v in vertices():
        other = _criteria(profile, _vertex_allocation(v))
        row = []
        for x, y in zip(target, other):
            scaled = (x - y) * 12
            assert scaled.denominator == 1
            row.append(scaled.numerator)
        diffs.append(tuple(row))
    for denominator in range(9, 16):
        for nums in _positive_compositions(denominator):
            if all(sum(d[k] * nums[k] for k in range(9)) >= 0 for d in diffs):
                return tuple(F(n, denominator) for n in nums)
    raise AssertionError(f"No positive support found for {profile}")


def verify_supported_oe(profile):
    weights = support_weights(tuple(profile))
    return len(weights) == 9 and min(weights) > 0
