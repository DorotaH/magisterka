import sys
import math


def can_win(h, n, a):
    # Create a list to store the factors of h
    factors = list()

    # Find all factors of h
    for i in range(1, 1 + int(math.sqrt(h))):
        if h % i == 0:
            factors.append(i)
            factors.append(h // i)

    # Sort the factors in ascending order
    factors.sort()

    # Check if h can be represented as a sum of distinct Ai
    for f in factors:
        used, sum_a = set(), 0
        for i in range(0, n):
            if h - f >= a[i]:
                sum_a += a[i]
                used.add(a[i])
            if sum_a == f:
                if len(used) == len(a):
                    return "Yes"
                for i in range(0, n):
                    if a[i] not in used:
                        used.add(a[i])
                        sum_a = sum_a + a[i]
                        if h == sum_a:
                            return "Yes"
                used.clear()
                sum_a = 0

    return "No"


h, n = map(int, input().split())
a = list(map(int, input().split()))
print(can_win(h, n, a))
