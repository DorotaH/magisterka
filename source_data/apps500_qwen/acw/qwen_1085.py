MOD = 998244353


def count_ways(n, k, len, arr):
	dp = [0] * (1 + n)
	dp[0] = 1
	for i in range(n):
		if arr[i] == -1:
			dp[i + 1] = 0
			for j in range(1, k + 1):
				dp[i + 1] += dp[i] if i - len >= 0 and arr[i - len] == j else dp[i] * k
				dp[i + 1] %= MOD
		else:
			dp[i + 1] = dp[i]
	return dp[n]


# Read input
n, k, len = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(count_ways(n, k, len, arr))
