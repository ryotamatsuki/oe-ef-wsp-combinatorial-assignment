"""Closed-form mechanism for the arbitrary-n, two-good acceptable-singletons theorem."""
from fractions import Fraction as F


def group_allocation(groups):
    """Return rows (a,b,ab,empty); True=L (a>b), False=R (b>a).

    The rule is the two-singleton eating allocation with total nonempty mass 2/n,
    zero probability on ab, and outside probability 1-2/n.
    """
    n = len(groups)
    if n < 2:
        raise ValueError("n must be at least 2")
    k = sum(groups)
    h = F(2, n)
    z = F(1) - h
    out = []
    for is_left in groups:
        if k == 0 or k == n:
            p = q = F(1, n)
        elif 2 * k < n:
            if is_left:
                p, q = h, F(0)
            else:
                q = F(1, n - k)
                p = h - q
        elif 2 * k > n:
            if is_left:
                p = F(1, k)
                q = h - p
            else:
                p, q = F(0), h
        else:
            if is_left:
                p, q = h, F(0)
            else:
                p, q = F(0), h
        out.append((p, q, F(0), z))
    return tuple(out)
