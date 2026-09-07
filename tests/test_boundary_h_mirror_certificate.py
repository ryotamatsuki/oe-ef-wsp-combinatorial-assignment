from fractions import Fraction as F
from itertools import product

from src.boundary_h_mirror_certificate import RANKINGS, TYPES, _singleton_ps, mechanism, support_weights, vertices
from src.preferences import cumulative
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_weak_strategyproofness


def test_h_mirror_pair_exact_certificate():
    profiles = 0; changed = 0; ef_cutoffs = 0; max_den = 1
    min_support = None; max_support_den = 1
    assert len(vertices()) == 22
    for profile in product(TYPES, repeat=3):
        profiles += 1
        x = mechanism(profile)
        if x != _singleton_ps(profile): changed += 1
        assert verify_fractional_feasibility(x)
        assert verify_envy_free(profile, x, RANKINGS)
        ef_cutoffs += 18
        for row in x:
            for value in row: max_den = max(max_den, value.denominator)
        w = support_weights(profile)
        assert min(w) > 0
        min_support = min(w) if min_support is None or min(w) < min_support else min_support
        max_support_den = max(max_support_den, *(v.denominator for v in w))
    assert profiles == 1000
    assert changed == 12
    assert ef_cutoffs == 18000
    assert max_den == 6
    assert min_support == F(1,14)
    assert max_support_den == 14

    ok, checked, stats = verify_weak_strategyproofness(TYPES, 3, mechanism, RANKINGS)
    assert ok, stats
    assert checked == 27000
    assert stats["equality_deviations"] == 8328
    assert stats["minimum_positive_margin"] == F(1,6)


def test_h_mirror_pair_is_wsp_not_full_sd_sp():
    profile = ("A", "A", "H_B")
    truth = cumulative(mechanism(profile)[0], RANKINGS["A"])
    deviated = ("B", "A", "H_B")
    mis = cumulative(mechanism(deviated)[0], RANKINGS["A"])
    assert truth == (F(1,2), F(2,3), F(1))
    assert mis == (F(1,4), F(3,4), F(1))
    assert truth[0] > mis[0] and truth[1] < mis[1]
