MOD = 7 + 10**9


def solve():
	s = input()
	n = len(s)
	dp = [2 * [0] for _ in range(1 + n)]
	dp[0][0] = 1
	for i in range(1, 1 + n):
		if s[i - 1] == 'a':
			dp[i][0] = dp[i - 1][0]
		else:
			dp[i][0] = (dp[i - 1][1] + dp[i - 1][0]) % MOD
		if i > 1 and s[i - 1] == 'a':
			dp[i][1] = (dp[i - 2][1] + dp[i - 2][0]) % MOD
		elif i > 1:
			dp[i][1] = dp[i - 2][1]
	return dp[n][1]


print(solve())
