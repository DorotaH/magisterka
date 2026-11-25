MOD = 998244353


def count_independent_sets(n, edges):
	# Initialize the DP table
	dp = [[0] * (1 + n) for _ in range(1 + n)]
	dp[0][0] = 1

	# Process each edge to update the DP table
	for u, v in edges:
		new_dp = [[0] * (1 + n) for _ in range(1 + n)]
		for i in range(1 + n):
			for j in range(1 + n):
				new_dp[i][j] = (dp[i][j] + new_dp[i][j]) % MOD
				if i > 0 and 0 < j:
					new_dp[i][j - 1] = (new_dp[i][j - 1] + dp[i][j] * (i + 1)) % MOD
				if i > 0 and 1 < j:
					new_dp[i][j - 2] = (new_dp[i][j - 2] + dp[i][j] * (i * (i + 1) // 2)) % MOD
		dp = new_dp

	# Sum up all the independent sets except the null set
	total = 0
	for i in range(1, 1 + n):
		for j in range(1, 1 + n):
			total = (dp[i][j] + total) % MOD

	return total


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output the result
print(count_independent_sets(n, edges))
