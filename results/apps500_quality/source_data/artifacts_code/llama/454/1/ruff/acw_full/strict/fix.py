M = 7 + 10**9


def odd_permutations(n, k):
	# Create a 2D array to store the number of permutations of oddness i modulo n
	dp = [[0] * (n * n + 1) for _ in range(1 + n)]

	# Initialize the base case
	dp[0][0] = 1

	# For each number of elements
	for i in range(1, 1 + n):
		# For each possible oddness
		for j in range(i, min(i * (i + 1) // 2 + 1, n * n + 1)):
			# If this is the first element, there are two ways to place it
			dp[i][j] = 1 if i == 1 else (dp[i - 1][j - i] + dp[i - 1][1 + j]) % M
	# Return the result
	return dp[n][k]


# Read the input
n, k = map(int, input().split())

# Print the result
print(odd_permutations(n, k))
