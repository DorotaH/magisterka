import sys
from fractions import Fraction


def min_resistors(a, b):
    target = Fraction(a, b)
    count = 0

    while target != 1:
        if not target > 1:
            # Try to make the target by adding a resistor in series
            if 1 / target - 1 > 0:
                count += 1
                target = 1 / (1 / target - 1)
        else:
            # Try to make the target by adding a resistor in parallel
            if target - 1 > 0:
                count += 1
                target -= 1

    return 1 + count

# Read input
a, b = map(int, sys.stdin.read().split())

# Output the result
print(min_resistors(a, b))
