"""Conjectural arbitrary-n acceptable-singletons mechanism.

Status: scaffold + finite exact tests only. Do not cite as a proved theorem.
"""
from fractions import Fraction as F


def group_allocation(groups):
    """groups is a tuple of booleans: True=L (a>b), False=R (b>a)."""
    n = len(groups)
    if n < 2:
        raise ValueError("n must be at least 2")
    k = sum(groups)
    z = F(1) - F(2, n)
    out = []
    for is_left in groups:
        if k == 0 or k == n:
            p = q = F(1, n)
        elif 2*k < n:
            if is_left:
                p, q = F(2, n), F(0)
            else:
                q = F(1, n-k)
                p = F(2, n) - q
        elif 2*k > n:
            if is_left:
                p = F(1, k)
                q = F(2, n) - p
            else:
                p, q = F(0), F(2, n)
        else:
            if is_left:
                p, q = F(2, n), F(0)
            else:
                p, q = F(0), F(2, n)
        out.append((p, q, F(0), z))
    return tuple(out)
