

def solve():
	n, l, r = map(int, input().split())
	dp = [2 * [0] for _ in range(2 + n)]
	dp[1][0] = 1
	dp[1][1] = 0

	for i in range(2, 2 + n):
		if i % 2 == 0:
			dp[i][0] = 0
			dp[i][1] = 1
		else:
			dp[i][0] = 1
			dp[i][1] = 0

	for i in range(2, 2 + n):
		if i % 2 == 0:
			dp[i][0] = 1
			dp[i][1] = 0
		else:
			dp[i][0] = 0
			dp[i][1] = 1

	for i in range(2, 2 + n):
		if i % 2 == 0:
			dp[i][0] += dp[i - 2][0]
			dp[i][1] += dp[i - 2][1]
		else:
			dp[i][0] += dp[i - 1][0]
			dp[i][1] += dp[i - 1][1]

	for i in range(2, 2 + n):
		if i % 2 == 0:
			dp[i][0] += dp[i - 2][0]
			dp[i][1] += dp[i - 2][1]
		else:
			dp[i][0] += dp[i - 1][0]
			dp[i][1] += dp[i - 1][1]

	print(dp[r][0])


solve()
