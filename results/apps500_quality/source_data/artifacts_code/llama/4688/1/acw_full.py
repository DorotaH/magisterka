import sys

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(1 + n)]
dp[0][0] = 1

for i in range(1, 1 + n):
	for j in range(1, k + 1):
		dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1])

print(dp[n][k])
