"""Canonical preference definitions for the 3-agent, 2-good project."""

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
