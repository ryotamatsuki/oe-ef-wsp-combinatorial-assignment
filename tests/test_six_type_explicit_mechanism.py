from itertools import product
from src.preferences import SIX_TYPE_RANKINGS
from src.mechanism_six_type import six_type_mechanism
from src.verify_feasibility import verify_fractional_feasibility
from src.verify_ef import verify_envy_free
from src.verify_wsp import verify_full_sd_strategyproofness
from src.verify_oe import six_type_analytic_oe, lp_sd_improvement_gain


def test_preference_rankings():
    assert set(SIX_TYPE_RANKINGS) == {"A","B","E","F","C","D"}
    assert all(len(set(r)) == 4 for r in SIX_TYPE_RANKINGS.values())


def test_six_type_explicit_mechanism():
    profiles = 0
    ef_cutoffs = 0
    for profile in product(SIX_TYPE_RANKINGS, repeat=3):
        profiles += 1
        x = six_type_mechanism(profile)
        assert verify_fractional_feasibility(x)
        assert verify_envy_free(profile, x, SIX_TYPE_RANKINGS)
        assert six_type_analytic_oe(x, profile)
        ef_cutoffs += 3 * 3 * 2
    assert profiles == 216
    assert ef_cutoffs == 3888


def test_six_type_full_sd_strategyproof():
    ok, checked, failure = verify_full_sd_strategyproofness(
        tuple(SIX_TYPE_RANKINGS), 3, six_type_mechanism, SIX_TYPE_RANKINGS
    )
    assert ok, failure
    assert checked == 3240


def test_six_type_oe_lp_self_attack():
    max_gain = 0.0
    for profile in product(SIX_TYPE_RANKINGS, repeat=3):
        max_gain = max(max_gain, lp_sd_improvement_gain(profile, six_type_mechanism(profile), SIX_TYPE_RANKINGS))
    assert max_gain < 1e-8
