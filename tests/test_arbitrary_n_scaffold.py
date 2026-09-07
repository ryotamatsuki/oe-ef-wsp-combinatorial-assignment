from itertools import product
from src.candidate_arbitrary_n import group_allocation
from src.preferences import EIGHT_TYPE_ACCEPTABLE_SINGLETONS, LEFT_EIGHT, cumulative


def test_arbitrary_n_scaffold_exact_n_2_to_10():
    ranks = EIGHT_TYPE_ACCEPTABLE_SINGLETONS
    for n in range(2, 11):
        for groups in product((False, True), repeat=n):
            x = group_allocation(groups)
            assert all(min(row) >= 0 and sum(row) == 1 for row in x)
            assert sum(row[0] for row in x) == 1
            assert sum(row[1] for row in x) == 1
            for i, group in enumerate(groups):
                true_types = [t for t in ranks if (t in LEFT_EIGHT) == group]
                for true_type in true_types:
                    own = cumulative(x[i], ranks[true_type])
                    for j in range(n):
                        other = cumulative(x[j], ranks[true_type])
                        assert all(a >= b for a, b in zip(own, other))
                    for misreport in ranks:
                        if misreport == true_type:
                            continue
                        changed = list(groups)
                        changed[i] = misreport in LEFT_EIGHT
                        mis = cumulative(group_allocation(tuple(changed))[i], ranks[true_type])
                        assert all(a >= b for a, b in zip(own, mis))
