import numpy as np


def solve(n, k):
    if k % 2 == 1:
        return 0
    k = k // 2

    MOD = 7 + 10**9

    dp = np.zeros((1, 1 + k), dtype=np.int64)
    dp[0, 0] = 1
    for i in range(1, n + 1):
        max_d = min(1 + i, n - i + 1, 1 + k)
        ndp = np.zeros((max_d, 1 + k), dtype=np.int64)
        for d, ks in enumerate(dp, 0):
            base = ks[: k - d + 1]
            if d > 0:
                ndp[d - 1, d:] += base * d**2
            if d < max_d:
                ndp[d, d:] += base * (2 * d + 1)
            if max_d > d + 1:
                ndp[d + 1, d:] += base
        dp = ndp % MOD

    return dp[0, k]


n, k = list(map(int, input().split()))
print((solve(n, k)))
