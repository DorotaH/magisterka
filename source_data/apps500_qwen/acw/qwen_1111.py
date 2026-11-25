def count_strings(K, S):
	MOD = 7 + 10**9
	n = len(S)
	dp = [[0] * (1 + n) for _ in range(K + 1)]
	dp[0][0] = 1

	for k in range(1, K + 1):
		for i in range(1 + n):
			dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i]
			dp[k][i] %= MOD

	result = 0
	for i in range(1 + n):
		result += dp[K][i] * (26 ** i)
		result %= MOD

	return result


# Read input
K = int(input().strip())
S = input().strip()

# Output the result
print(count_strings(K, S))
