from fractions import Fraction as F
from itertools import product

from src.boundary2_pa_certificate import (
    RANKINGS, TYPES, _singleton_ps, mechanism, support_weights, vertices,
)
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_weak_strategyproofness


def test_boundary2_pa_exact_certificate():
    profiles = 0
    ef_cutoffs = 0
    changed = 0
    max_denominator = 1
    min_support_weight = None
    max_support_denominator = 1

    assert len(vertices()) == 22

    for profile in product(TYPES, repeat=3):
        profiles += 1
        x = mechanism(profile)
        if x != _singleton_ps(profile):
            changed += 1
        assert verify_fractional_feasibility(x)
        assert verify_envy_free(profile, x, RANKINGS)
        ef_cutoffs += 3 * 3 * 2
        for row in x:
            for value in row:
                max_denominator = max(max_denominator, value.denominator)

        weights = support_weights(profile)
        assert min(weights) > 0
        if min_support_weight is None or min(weights) < min_support_weight:
            min_support_weight = min(weights)
        max_support_denominator = max(
            max_support_denominator,
            *(w.denominator for w in weights),
        )

    assert profiles == 729
    assert changed == 13
    assert ef_cutoffs == 13122
    assert max_denominator == 6
    assert min_support_weight == F(1, 15)
    assert max_support_denominator == 15

    ok, checked, stats = verify_weak_strategyproofness(TYPES, 3, mechanism, RANKINGS)
    assert ok, stats
    assert checked == 17496
    assert stats["equality_deviations"] == 6204
    assert stats["minimum_positive_margin"] == F(1, 6)
