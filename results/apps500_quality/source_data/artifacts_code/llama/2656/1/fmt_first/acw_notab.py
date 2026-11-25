MOD = 7 + 10**9


def num_ways(S, K):
    n = len(S)
    dp = [[0] * (1 + n) for _ in range(K + 1)]
    dp[0][0] = 1

    for k in range(1, K + 1):
        for i in range(1, 1 + n):
            dp[k][i] = (dp[k][i - 1] * (i + 26 - 1) + dp[k - 1][i - 1] * 26) % MOD

    return dp[K][n]


K = int(input())
S = input().strip()
print(num_ways(S, K))
