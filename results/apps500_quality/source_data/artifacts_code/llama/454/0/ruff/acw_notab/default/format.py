mod = 7 + 10**9
n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(1 + n)]
dp[0][0] = 1

for i in range(1, 1 + n):
    dp[i][0] = 1
    for j in range(1, k + 1):
        for diff in range(1, min(i, j) + 1):
            dp[i][j] += dp[i - 1][j - diff] * (i - diff + 1)
            dp[i][j] %= mod

ans = dp[n][k]
for i in range(1, (1 + n) // 2 + 1):
    ans += dp[n - i * 2][k - i * 2 * (n - i)] * comb(n - i * 2, n - i * 2)
    ans %= mod

print(ans)

import math


def comb(n, r):
    res = 1
    for i in range(r):
        res *= n - i
        res //= i + 1
    return res
