from itertools import product
from .preferences import cumulative


def verify_full_sd_strategyproofness(types, n_agents, mechanism, rankings):
    checked = 0
    for profile in product(types, repeat=n_agents):
        truthful_allocation = mechanism(profile)
        for i, true_type in enumerate(profile):
            truth = cumulative(truthful_allocation[i], rankings[true_type])
            for misreport in types:
                if misreport == true_type:
                    continue
                deviated = list(profile)
                deviated[i] = misreport
                deviated = tuple(deviated)
                mis = cumulative(mechanism(deviated)[i], rankings[true_type])
                checked += 1
                if any(a < b for a, b in zip(truth, mis)):
                    return False, checked, (profile, i, true_type, misreport, truth, mis)
    return True, checked, None


def verify_weak_strategyproofness(types, n_agents, mechanism, rankings):
    """Exact WSP: no misreport allocation strictly bundle-SD dominates truth."""
    checked = 0
    equality_deviations = 0
    minimum_positive_margin = None
    for profile in product(types, repeat=n_agents):
        truthful_allocation = mechanism(profile)
        for i, true_type in enumerate(profile):
            truth = cumulative(truthful_allocation[i], rankings[true_type])
            for misreport in types:
                if misreport == true_type:
                    continue
                deviated = list(profile)
                deviated[i] = misreport
                deviated = tuple(deviated)
                mis = cumulative(mechanism(deviated)[i], rankings[true_type])
                checked += 1
                differences = tuple(a - b for a, b in zip(truth, mis))
                if all(d == 0 for d in differences):
                    equality_deviations += 1
                    continue
                if all(d <= 0 for d in differences) and any(d < 0 for d in differences):
                    return False, checked, {
                        "profile": profile,
                        "agent": i,
                        "true_type": true_type,
                        "misreport": misreport,
                        "truth": truth,
                        "mis": mis,
                    }
                margin = max(differences)
                if margin <= 0:
                    return False, checked, (profile, i, true_type, misreport, differences)
                if minimum_positive_margin is None or margin < minimum_positive_margin:
                    minimum_positive_margin = margin
    return True, checked, {
        "equality_deviations": equality_deviations,
        "minimum_positive_margin": minimum_positive_margin,
    }
