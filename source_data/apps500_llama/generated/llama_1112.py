MOD = 10**9 + 7

def num_ways(S, K):
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(K + 1)]
    dp[0][0] = 1

    for k in range(1, K + 1):
        for i in range(1, n + 1):
            dp[k][i] = (dp[k][i - 1] * (26 + i - 1) + dp[k - 1][i - 1] * 26) % MOD

    return dp[K][n]

K = int(input())
S = input().strip()
print(num_ways(S, K))
