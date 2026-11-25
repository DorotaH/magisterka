from collections import defaultdict
from math import isqrt


def min_subsequence_length(a):
    n = len(a)
    dp = [1 + n] * (1 << 20)
    dp[0] = 0
    divisors = defaultdict(list)

    def get_divisors(x):
        for i in range(1, isqrt(x) + 1):
            if 0 == x % i:
                divisors[i].append(x // i)
                if i * i != x:
                    divisors[x // i].append(i)

    for x in a:
        get_divisors(x)

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                new_mask = mask ^ (1 << i)
                for d in divisors[a[i]]:
                    if new_mask & (1 << (d - 1)):
                        dp[mask] = min(dp[mask], 1 + dp[new_mask])

    min_length = min(dp)
    return min_length if min_length < 1 + n else -1


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(min_subsequence_length(a))
