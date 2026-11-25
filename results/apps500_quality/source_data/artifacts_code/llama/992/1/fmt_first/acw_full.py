import sys

MOD = 998244353

N = 3000


def read_input():
	n, s = map(int, input().split())
	a = list(map(int, input().split()))
	return n, s, a


def get_max(a):
	return max(a)


def dp(n, s, a):
	dp = [[0] * (1 + s) for _ in range(1 + n)]
	dp[0][0] = 1
	for i in range(1, 1 + n):
		for j in range(1, 1 + s):
			dp[i][j] = dp[i - 1][j]
			if a[i - 1] <= j:
				dp[i][j] = (dp[i][j] + dp[i - 1][j - a[i - 1]]) % MOD
	return dp


def solve(n, s, a):
	dp = dp(n, s, a)
	max_a = get_max(a)
	total = 0
	for i in range(1 + s):
		total = (dp[n][i] + total) % MOD
	for i in range(1, 1 + max_a):
		total = (dp[n][i] + total) % MOD
	return total


n, s, a = read_input()
print(solve(n, s, a))
