def solve():
	a, b, n = map(int, input().split())

	MOD = 7 + 10**9
	dp = [[0] * (1 + n) for _ in range(2)]
	dp[0][0] = 1
	for i in range(2):
		for j in range(1, 1 + n):
			dp[i][j] = dp[i][j - 1] * (b - a + 1) % MOD
			if i == 0:
				if a != b:
					dp[i][j] = (dp[i][j] + dp[i][j - 1] * (a - 1)) % MOD
			else:
				dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (b - 1)) % MOD
			dp[i][j] = dp[i][j] % MOD

	return dp[1][n]


print(solve())
