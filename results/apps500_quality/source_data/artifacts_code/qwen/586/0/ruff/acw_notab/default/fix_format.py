MOD = 998244353


def count_suitable_colorings(n, k):
    if n == 1:
        return 0
    if k == 1:
        return 1

    dp = [[2 * [0] for _ in range(2)] for _ in range(n)]
    dp[0][0][0] = 1
    dp[0][0][1] = 1

    for i in range(1, n):
        dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1]) % MOD
        dp[i][0][1] = (dp[i - 1][0][0] + dp[i - 1][0][1]) % MOD
        dp[i][1][0] = (dp[i - 1][1][0] + dp[i - 1][1][1]) % MOD
        dp[i][1][1] = (dp[i - 1][1][0] + dp[i - 1][1][1]) % MOD

    total = (
        dp[n - 1][0][0] + dp[n - 1][0][1] + dp[n - 1][1][0] + dp[n - 1][1][1]
    ) % MOD

    for i in range(n):
        for j in range(n):
            if i + j >= k:
                total -= dp[i][j][1] + dp[i][j][0]
                total += dp[i][j][1] * dp[i][j][0]
                total %= MOD

    return total


import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])

print(count_suitable_colorings(n, k))
