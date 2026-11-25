import sys


def solve():
	n, m = map(int, sys.stdin.readline().split())
	d = list(map(int, sys.stdin.readline().split()))
	g, r = map(int, sys.stdin.readline().split())

	d.sort()
	d = [0] + d + [n]

	if d[-1] == 0:
		print(-1)
		return

	dp = [[float('inf')] * (1 + n) for _ in range(1 + n)]
	dp[0][0] = 0

	for i in range(1, 1 + n):
		for j in range(1 + n):
			if dp[i - 1][j] != float('inf'):
				if j != 0:
					dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
				if i >= 2:
					dp[i][j - 1] = min(dp[i][j - 1], 1 + dp[i - 1][j])
				if j != n:
					dp[i][1 + j] = min(dp[i][1 + j], 1 + dp[i - 1][j])

	for i in range(1, 1 + m):
		if g < d[i] - d[i - 1]:
			print(-1)
			return

		for j in range(1 + n):
			if j != 0:
				dp[d[i - 1]][j] = min(dp[d[i - 1]][j], dp[g + d[i - 1]][j] + g)
			if j != n:
				dp[d[i - 1]][1 + j] = min(dp[d[i - 1]][1 + j], dp[g + d[i - 1]][j] + g)
			if j != 0:
				dp[d[i - 1]][j - 1] = min(dp[d[i - 1]][j - 1], dp[g + d[i - 1]][j] + g)

	ans = float('inf')
	for i in range(1 + n):
		if dp[n][i] != float('inf'):
			ans = min(ans, dp[n][i] + (n - d[-2]) // g * (g + r) + (n - d[-2]) % g)

	if ans == float('inf'):
		print(-1)
	else:
		print(ans)


solve()
