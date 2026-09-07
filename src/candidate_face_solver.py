"""Regression gate for candidate-face solvers.

The historical candidate-face implementation that produced the invalid INFEASIBLE
claim is not present in the repository or available artifacts. This module therefore
does not pretend to reconstruct that legacy code. It provides a hard acceptance gate:
any future candidate-face implementation must accept the known-good explicit witness.
"""

from itertools import product
from .preferences import SIX_TYPE_RANKINGS
from .mechanism_six_type import six_type_mechanism
from .verify_feasibility import verify_fractional_feasibility
from .verify_ef import verify_envy_free
from .verify_oe import six_type_analytic_oe


def known_good_witness_is_accepted():
    for profile in product(SIX_TYPE_RANKINGS, repeat=3):
        allocation = six_type_mechanism(profile)
        if not verify_fractional_feasibility(allocation):
            return False, ("feasibility", profile)
        if not verify_envy_free(profile, allocation, SIX_TYPE_RANKINGS):
            return False, ("EF", profile)
        if not six_type_analytic_oe(allocation, profile):
            return False, ("OE", profile)
    return True, None


def solve_six_type_baseline():
    """Return SAT with the explicit witness; not a general-purpose face search."""
    ok, failure = known_good_witness_is_accepted()
    if not ok:
        return {"status": "ERROR", "failure": failure}
    return {"status": "SAT", "mechanism": "explicit_astra_rule", "profiles": 216}
