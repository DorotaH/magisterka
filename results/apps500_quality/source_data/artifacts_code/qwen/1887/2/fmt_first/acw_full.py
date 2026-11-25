def max_team_height(n, h1, h2):
	dp = [[0] * (1 + n) for _ in range(1 + n)]

	for i in range(1, 1 + n):
		for j in range(1, 1 + n):
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
			if i > 1:
				dp[i][j] = max(dp[i][j], h2[i - 1] + dp[i - 1][j - 1])
			if 1 < j:
				dp[i][j] = max(dp[i][j], h1[j - 1] + dp[i][j - 1])
			if i > 1 and 1 < j:
				dp[i][j] = max(dp[i][j], h1[j - 1] + dp[i - 1][j - 1] + h2[i - 1])

	return dp[n][n]


# Read input
n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

# Calculate and print the result
print(max_team_height(n, h1, h2))
