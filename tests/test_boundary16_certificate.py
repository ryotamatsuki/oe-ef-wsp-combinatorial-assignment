from fractions import Fraction as F
from itertools import combinations_with_replacement, product

from src.boundary16_certificate import (
    RANKINGS, TYPES, mechanism, singleton_ps, support_weights, vertices,
)
from src.preferences import cumulative
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_weak_strategyproofness


def test_boundary16_exact_certificate():
    profiles = 0
    changed = 0
    ef_cutoffs = 0
    max_allocation_denominator = 1

    assert len(TYPES) == 16
    assert len(vertices()) == 22

    for profile in product(TYPES, repeat=3):
        profiles += 1
        x = mechanism(profile)
        if x != singleton_ps(profile):
            changed += 1
        assert verify_fractional_feasibility(x)
        assert verify_envy_free(profile, x, RANKINGS)
        ef_cutoffs += 3 * 2 * 3
        for row in x:
            for value in row:
                max_allocation_denominator = max(max_allocation_denominator, value.denominator)

    assert profiles == 4096
    assert changed == 488
    assert ef_cutoffs == 73728
    assert max_allocation_denominator == 6

    ok, checked, stats = verify_weak_strategyproofness(TYPES, 3, mechanism, RANKINGS)
    assert ok, stats
    assert checked == 184320
    assert stats["equality_deviations"] == 44400
    assert stats["minimum_positive_margin"] == F(1, 6)


def test_boundary16_exact_continuous_oe_support():
    # The mechanism is anonymous. It suffices to certify one representative of
    # each agent-permutation class; support vectors permute with agents.
    canonical_profiles = 0
    min_support_weight = None
    max_support_denominator = 1
    for profile in combinations_with_replacement(TYPES, 3):
        canonical_profiles += 1
        w = support_weights(profile)
        assert min(w) > 0
        mw = min(w)
        if min_support_weight is None or mw < min_support_weight:
            min_support_weight = mw
        max_support_denominator = max(max_support_denominator, *(x.denominator for x in w))

    assert canonical_profiles == 816
    assert min_support_weight == F(1, 15)
    assert max_support_denominator == 19


def test_boundary16_is_wsp_not_full_sd_sp():
    truth_profile = ("A", "A", "H_B")
    mis_profile = ("B", "A", "H_B")
    truth = cumulative(mechanism(truth_profile)[0], RANKINGS["A"])
    mis = cumulative(mechanism(mis_profile)[0], RANKINGS["A"])
    assert truth == (F(1,2), F(2,3), F(1))
    assert mis == (F(1,4), F(3,4), F(1))
    assert truth[0] > mis[0] and truth[1] < mis[1]
