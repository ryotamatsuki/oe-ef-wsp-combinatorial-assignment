from itertools import product
from src.preferences import EIGHT_TYPE_ACCEPTABLE_SINGLETONS, ONE_SINGLETON_UNACCEPTABLE
from src.boundary1_certificate import boundary1_mechanism
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_weak_strategyproofness
from src.verify_oe import lp_sd_improvement_gain

RANKINGS = {
    **EIGHT_TYPE_ACCEPTABLE_SINGLETONS,
    "H_A": ONE_SINGLETON_UNACCEPTABLE["H_A"],
}
TYPES = tuple(RANKINGS)


def test_boundary1_exact_feasibility_ef_wsp():
    profiles = 0
    ef_cutoffs = 0
    for profile in product(TYPES, repeat=3):
        profiles += 1
        allocation = boundary1_mechanism(profile)
        assert verify_fractional_feasibility(allocation)
        assert verify_envy_free(profile, allocation, RANKINGS)
        ef_cutoffs += 3 * 2 * 3
    assert profiles == 729
    assert ef_cutoffs == 13122

    ok, checked, details = verify_weak_strategyproofness(
        TYPES, 3, boundary1_mechanism, RANKINGS
    )
    assert ok, details
    assert checked == 17496
    assert details["equality_deviations"] == 5970
    assert details["minimum_positive_margin"].numerator == 1
    assert details["minimum_positive_margin"].denominator == 1000


def test_boundary1_oe_continuous_self_attack():
    max_gain = 0.0
    for profile in product(TYPES, repeat=3):
        allocation = boundary1_mechanism(profile)
        gain = lp_sd_improvement_gain(profile, allocation, RANKINGS)
        max_gain = max(max_gain, gain)
    assert max_gain < 1e-8
