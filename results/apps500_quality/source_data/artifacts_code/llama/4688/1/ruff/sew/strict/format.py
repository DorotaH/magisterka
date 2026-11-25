import sys

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, 1 + n):
    for j in range(1, 1 + k):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k])
