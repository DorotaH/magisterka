from fractions import Fraction
from itertools import combinations_with_replacement


def min_volume(n, k, a):
    n = Fraction(n, 1000)
    a = sorted([Fraction(a_i, 1000) for a_i in a])

    for r in range(1, k + 1):
        for combo in combinations_with_replacement(a, r):
            if sum(combo) == n:
                return r
    return -1

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(min_volume(n, k, a))
