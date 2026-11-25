MOD = 998244353


def count_ways(n, k, len, arr):
	dp = [[0] * (k + 1) for _ in range(1 + n)]
	dp[0][0] = 1

	for i in range(n):
		for j in range(1, k + 1):
			if arr[i] != -1 and arr[i] == j:
				dp[i + 1][j] = dp[i][j]
			else:
				for l in range(max(0, i - len + 1), i + 1):
					dp[i + 1][j] = (dp[i + 1][j] + dp[l][j]) % MOD

	return sum(dp[n]) % MOD


# Read input
n, k, len = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(count_ways(n, k, len, arr))
