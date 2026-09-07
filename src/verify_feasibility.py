from fractions import Fraction as F

def verify_fractional_feasibility(allocation):
    for row in allocation:
        if min(row) < 0 or sum(row) != 1:
            return False
    use_a = sum(row[0] + row[2] for row in allocation)
    use_b = sum(row[1] + row[2] for row in allocation)
    return use_a <= F(1) and use_b <= F(1)
