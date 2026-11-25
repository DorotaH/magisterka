import math
import sys


def solve(n):
	if n == 0:
		return 0
	dp = [0] * (2 * n + 1)
	dp[1] = 2
	dp[2] = 4
	for i in range(3, 2 * n + 1):
		dp[i] = dp[i - 1] + 4 * (i // 2 + 1) - (i // 4) * 4
	return dp[2 * n]


n = int(input())
print(solve(n))
