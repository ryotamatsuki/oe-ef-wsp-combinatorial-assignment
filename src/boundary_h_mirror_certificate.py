"""Exact certificate for D8_ACCEPTABLE_SINGLETONS + {H_A,H_B} (n=3).

H_A: a > ab > empty > b
H_B: b > ab > empty > a

The mechanism is singleton PS except at 12 ordered profiles: permutations of
(X,H_A,H_A) and (X,H_B,H_B) for X in {C,D}. OE is certified exactly by
positive rational SD scalarizations against the complete 22-vertex continuous
fractional feasible polytope.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations

from .preferences import BUNDLES, EIGHT_TYPE_ACCEPTABLE_SINGLETONS, ONE_SINGLETON_UNACCEPTABLE, cumulative

RANKINGS = {
    **EIGHT_TYPE_ACCEPTABLE_SINGLETONS,
    "H_A": ONE_SINGLETON_UNACCEPTABLE["H_A"],
    "H_B": ONE_SINGLETON_UNACCEPTABLE["H_B"],
}
TYPES = tuple(RANKINGS)


def _singleton_ps(profile):
    profile = tuple(profile)
    remaining = {"a": F(1), "b": F(1)}
    alloc = [{"a": F(0), "b": F(0), "empty": F(0)} for _ in profile]
    restricted = {t: tuple(x for x in RANKINGS[t] if x in ("a", "b", "empty")) for t in set(profile)}
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


_HA_ROW = (F(1,3), F(0), F(0), F(2,3))
_HB_ROW = (F(0), F(1,3), F(0), F(2,3))
_LEFT_PAIR_ROW = (F(0), F(2,3), F(1,3), F(0))
_RIGHT_PAIR_ROW = (F(2,3), F(0), F(1,3), F(0))


def mechanism(profile):
    """Exact OE+EF+WSP mechanism on the H_A/H_B mirror-pair boundary domain."""
    profile = tuple(profile)
    if profile.count("H_A") == 2 and any(t in {"C", "D"} for t in profile):
        return tuple(_LEFT_PAIR_ROW if t in {"C", "D"} else _HA_ROW for t in profile)
    if profile.count("H_B") == 2 and any(t in {"C", "D"} for t in profile):
        return tuple(_RIGHT_PAIR_ROW if t in {"C", "D"} else _HB_ROW for t in profile)
    return _singleton_ps(profile)


def _facets():
    A, b = [], []
    for j in range(9):
        row = [0] * 9; row[j] = -1
        A.append(tuple(row)); b.append(0)
    for i in range(3):
        row = [0] * 9; row[3*i:3*i+3] = [1,1,1]
        A.append(tuple(row)); b.append(1)
    row = [0] * 9
    for i in range(3): row[3*i] = 1; row[3*i+2] = 1
    A.append(tuple(row)); b.append(1)
    row = [0] * 9
    for i in range(3): row[3*i+1] = 1; row[3*i+2] = 1
    A.append(tuple(row)); b.append(1)
    return tuple(A), tuple(b)


def _solve_square(rows, rhs):
    n = len(rhs)
    M = [[F(rows[i][j]) for j in range(n)] + [F(rhs[i])] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col] != 0), None)
        if pivot is None: return None
        if pivot != col: M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]; M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r == col: continue
            f = M[r][col]
            if f: M[r] = [M[r][j] - f * M[col][j] for j in range(n+1)]
    return tuple(M[i][-1] for i in range(n))


@lru_cache(maxsize=1)
def vertices():
    A, b = _facets(); out = set()
    for active in combinations(range(14), 9):
        sol = _solve_square([A[i] for i in active], [b[i] for i in active])
        if sol is None: continue
        if all(sum(F(row[j]) * sol[j] for j in range(9)) <= F(rhs) for row, rhs in zip(A,b)):
            out.add(sol)
    assert len(out) == 22
    return tuple(sorted(out))


def _vertex_allocation(v):
    rows = []
    for i in range(3):
        a,b,ab = v[3*i:3*i+3]
        rows.append((a,b,ab,F(1)-a-b-ab))
    return tuple(rows)


def _criteria(profile, allocation):
    vals = []
    for i,t in enumerate(profile): vals.extend(cumulative(allocation[i], RANKINGS[t]))
    return tuple(vals)


def _positive_compositions(total, parts=9):
    for cuts in combinations(range(1,total), parts-1):
        prev=0; vals=[]
        for cut in cuts + (total,):
            vals.append(cut-prev); prev=cut
        yield tuple(vals)


@lru_cache(maxsize=None)
def support_weights(profile):
    profile = tuple(profile); target = _criteria(profile, mechanism(profile)); diffs=[]
    for v in vertices():
        other = _criteria(profile, _vertex_allocation(v)); row=[]
        for x,y in zip(target,other):
            scaled=(x-y)*12
            assert scaled.denominator == 1
            row.append(scaled.numerator)
        diffs.append(tuple(row))
    for denominator in range(9,15):
        for nums in _positive_compositions(denominator):
            if all(sum(d[k]*nums[k] for k in range(9)) >= 0 for d in diffs):
                return tuple(F(n,denominator) for n in nums)
    raise AssertionError(f"No positive support found for {profile}")


def verify_supported_oe(profile):
    w = support_weights(tuple(profile))
    return len(w) == 9 and min(w) > 0
