from itertools import product
from src.preferences import EIGHT_TYPE_ACCEPTABLE_SINGLETONS
from src.mechanism_six_type import acceptable_singletons_mechanism
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_full_sd_strategyproofness
from src.verify_oe import lp_sd_improvement_gain


def test_acceptable_singleton_eight_type_mechanism():
    ranks = EIGHT_TYPE_ACCEPTABLE_SINGLETONS
    profiles = 0
    for profile in product(ranks, repeat=3):
        profiles += 1
        x = acceptable_singletons_mechanism(profile)
        assert verify_fractional_feasibility(x)
        assert verify_envy_free(profile, x, ranks)
        assert lp_sd_improvement_gain(profile, x, ranks) < 1e-8
    assert profiles == 512
    ok, checked, failure = verify_full_sd_strategyproofness(
        tuple(ranks), 3, acceptable_singletons_mechanism, ranks
    )
    assert ok, failure
    assert checked == 10752
