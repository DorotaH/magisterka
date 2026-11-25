MOD = 1000000007


def count_excellent_numbers(a, b, n):
	# Initialize a DP table where dp[i][j] represents the number of good numbers of length i with sum j
	dp = [[0] * (4 * n + 1) for _ in range(1 + n)]
	dp[0][0] = 1

	for i in range(1, 1 + n):
		for j in range(4 * n + 1):
			if a <= j:
				dp[i][j] = (dp[i][j] + dp[i - 1][j - a]) % MOD
			if b <= j:
				dp[i][j] = (dp[i - 1][j - b] + dp[i][j]) % MOD

	# Sum up all the ways to get a sum that is a good number
	result = 0
	for j in range(4 * n + 1):
		if all(x in {a, b} for x in str(j)):
			result = (result + dp[n][j]) % MOD

	return result


# Read input
a, b, n = map(int, input().split())

# Output the result
print(count_excellent_numbers(a, b, n))
