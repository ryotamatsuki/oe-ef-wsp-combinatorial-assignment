"""Singleton probabilistic-serial baseline for the first boundary domain.

The rule ignores bundle ab and runs PS on scarce singleton goods a,b plus an
unlimited outside option, using each reported bundle ranking restricted to
(a,b,empty).  It is a useful baseline but is not OE at three permutations of
(C,H_A,H_A); see boundary1_certificate.py for the exact repaired mechanism.
"""
from fractions import Fraction as F
from .preferences import EIGHT_TYPE_ACCEPTABLE_SINGLETONS, ONE_SINGLETON_UNACCEPTABLE

RANKINGS = {
    **EIGHT_TYPE_ACCEPTABLE_SINGLETONS,
    "H_A": ONE_SINGLETON_UNACCEPTABLE["H_A"],
}


def singleton_ps(profile):
    profile = tuple(profile)
    n = len(profile)
    remaining = {"a": F(1), "b": F(1)}
    allocations = [{"a": F(0), "b": F(0), "empty": F(0)} for _ in profile]
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
            allocations[i][choice] += dt
        for g in ("a", "b"):
            remaining[g] -= dt * rates[g]
        time += dt
    return tuple(
        (row["a"], row["b"], F(0), row["empty"])
        for row in allocations
    )
