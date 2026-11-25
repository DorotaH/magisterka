import math


def can_win(h, n, a):
    # Create a list to store the factors of h
    factors = []
    
    # Find all factors of h
    for i in range(1, int(math.sqrt(h)) + 1):
        if h % i == 0:
            factors.append(i)
            factors.append(h // i)

    # Sort the factors in ascending order
    factors.sort()

    # Check if h can be represented as a sum of distinct Ai
    for f in factors:
        used = set()
        sum_a = 0
        for i in range(n):
            if h - f >= a[i]:
                sum_a += a[i]
                used.add(a[i])
            if sum_a == f:
                if len(used) == len(a):
                    return "Yes"
                for i in range(n):
                    if a[i] not in used:
                        used.add(a[i])
                        sum_a += a[i]
                        if sum_a == h:
                            return "Yes"
                used.clear()
                sum_a = 0

    return "No"

h, n = map(int, input().split())
a = list(map(int, input().split()))
print(can_win(h, n, a))
