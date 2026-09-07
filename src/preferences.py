"""Canonical preference definitions for the two-good bundle-assignment project."""

BUNDLES = ("a", "b", "ab", "empty")

SIX_TYPE_RANKINGS = {
    "A": ("a", "b", "empty", "ab"),
    "B": ("b", "a", "empty", "ab"),
    "E": ("a", "ab", "b", "empty"),
    "F": ("b", "ab", "a", "empty"),
    "C": ("ab", "a", "b", "empty"),
    "D": ("ab", "b", "a", "empty"),
}

EIGHT_TYPE_ACCEPTABLE_SINGLETONS = {
    **SIX_TYPE_RANKINGS,
    "J": ("a", "b", "ab", "empty"),
    "K": ("b", "a", "ab", "empty"),
}

# Minimal boundary types: exactly one singleton is below the outside option.
# Mirror partners are obtained by swapping a and b.
ONE_SINGLETON_UNACCEPTABLE = {
    "H_A": ("a", "ab", "empty", "b"),
    "H_B": ("b", "ab", "empty", "a"),
    "P_A": ("ab", "a", "empty", "b"),
    "P_B": ("ab", "b", "empty", "a"),
    "U_A": ("a", "empty", "ab", "b"),
    "U_B": ("b", "empty", "ab", "a"),
    "W_A": ("a", "empty", "b", "ab"),
    "W_B": ("b", "empty", "a", "ab"),
}

# First both-singletons-unacceptable pair for the second boundary attack.
BOTH_SINGLETONS_UNACCEPTABLE_PAIR = {
    "T_A": ("ab", "empty", "a", "b"),
    "T_B": ("ab", "empty", "b", "a"),
}

LEFT_SIX = frozenset({"A", "E", "C"})
RIGHT_SIX = frozenset({"B", "F", "D"})
LEFT_EIGHT = frozenset(t for t, ranking in EIGHT_TYPE_ACCEPTABLE_SINGLETONS.items() if ranking.index("a") < ranking.index("b"))
RIGHT_EIGHT = frozenset(EIGHT_TYPE_ACCEPTABLE_SINGLETONS) - LEFT_EIGHT


def cumulative(row, ranking):
    """Return the three non-trivial bundle-SD cumulative cutoffs."""
    index = {b: i for i, b in enumerate(BUNDLES)}
    total = 0
    out = []
    for bundle in ranking[:-1]:
        total += row[index[bundle]]
        out.append(total)
    return tuple(out)
