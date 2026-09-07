from fractions import Fraction as F
from src.mechanism_arbitrary_n import group_allocation


def test_closed_form_counts_and_cross_group_incentives_n_2_to_100():
    for n in range(2, 101):
        h = F(2, n)
        for k in range(n + 1):
            groups = (True,) * k + (False,) * (n - k)
            x = group_allocation(groups)
            assert all(min(row) >= 0 and sum(row) == 1 for row in x)
            assert sum(row[0] for row in x) == 1
            assert sum(row[1] for row in x) == 1
            assert all(row[2] == 0 and row[0] + row[1] == h for row in x)

            if k >= 1:
                truthful_p = x[0][0]
                changed = list(groups)
                changed[0] = False
                mis_p = group_allocation(tuple(changed))[0][0]
                assert truthful_p >= mis_p

            if k <= n - 1:
                idx = k
                truthful_q = x[idx][1]
                changed = list(groups)
                changed[idx] = True
                mis_q = group_allocation(tuple(changed))[idx][1]
                assert truthful_q >= mis_q
