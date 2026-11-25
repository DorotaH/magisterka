import sys


def solve():
	n, b, a = map(int, sys.stdin.readline().split())
	s = list(map(int, sys.stdin.readline().split()))

	dp = [[0, 0] for _ in range(1 + n)]
	dp[0][0] = 0
	dp[0][1] = 0

	for i in range(1, 1 + n):
		dp[i][0] = -1
		dp[i][1] = -1

		if s[i - 1] == 1:
			if 0 < b:
				dp[i][0] = 1 + dp[i - 1][0]
			if i > 1 and a > 0:
				dp[i][1] = dp[i - 1][1] + 1
		else:
			if 0 < b:
				dp[i][0] = max(dp[i][0], 1 + dp[i - 1][0])
			if a > 0 and i > 1:
				dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)

		if 0 < b and a > 0 and s[i - 1] == 1:
			if dp[i - 1][1] < dp[i - 1][0]:
				dp[i][0] = max(dp[i][0], 1 + dp[i - 1][0] + min(b, a))
			else:
				dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1 + min(b, a))

	ans = max(dp[n][0], dp[n][1])
	print(ans)


if __name__ == "__main__":
	solve()
