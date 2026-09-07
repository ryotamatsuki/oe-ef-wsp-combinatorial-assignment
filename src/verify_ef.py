from .preferences import cumulative

def verify_envy_free(profile, allocation, rankings):
    for i, true_type in enumerate(profile):
        own = cumulative(allocation[i], rankings[true_type])
        for j in range(len(profile)):
            other = cumulative(allocation[j], rankings[true_type])
            if any(a < b for a, b in zip(own, other)):
                return False
    return True
