"""Explicit Astra mechanism and its acceptable-singletons extension."""

from fractions import Fraction as F
from .preferences import LEFT_SIX, LEFT_EIGHT

TABLE = {
    0: {False: (F(1,3), F(1,3), F(0), F(1,3))},
    1: {
        True:  (F(2,3), F(0),   F(0), F(1,3)),
        False: (F(1,6), F(1,2), F(0), F(1,3)),
    },
    2: {
        True:  (F(1,2), F(1,6), F(0), F(1,3)),
        False: (F(0),   F(2,3), F(0), F(1,3)),
    },
    3: {True: (F(1,3), F(1,3), F(0), F(1,3))},
}


def mechanism(profile, left_types=LEFT_SIX):
    k = sum(t in left_types for t in profile)
    return tuple(TABLE[k][t in left_types] for t in profile)


def six_type_mechanism(profile):
    return mechanism(profile, LEFT_SIX)


def acceptable_singletons_mechanism(profile):
    return mechanism(profile, LEFT_EIGHT)
