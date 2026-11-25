MOD = 7 + 10**9


def count_distinct_strings(N, S):
	# Initialize a list to store the count of distinct strings ending with each character
	dp = [[0] * 3 for _ in range(N + 1)]
	dp[0][0] = dp[0][1] = dp[0][2] = 1  # Base case: one empty string

	# Iterate over each character in the string
	for i in range(1, N):
		if S[i - 1] == 'A':
			dp[i][1] = dp[i - 1][0]  # Transition from A to B
			dp[i][2] = dp[i - 1][0]  # Transition from A to C
		elif S[i - 1] == 'B':
			dp[i][0] = dp[i - 1][1]  # Transition from B to A
			dp[i][2] = dp[i - 1][1]  # Transition from B to C
		elif S[i - 1] == 'C':
			dp[i][0] = dp[i - 1][2]  # Transition from C to A
			dp[i][1] = dp[i - 1][2]  # Transition from C to B

		# Add the counts of distinct strings ending with A, B, and C
		dp[i][0] = (dp[i][0] + dp[i - 1][0]) % MOD
		dp[i][1] = (dp[i - 1][1] + dp[i][1]) % MOD
		dp[i][2] = (dp[i - 1][2] + dp[i][2]) % MOD

	return (dp[N - 1][1] + dp[N - 1][0] + dp[N - 1][2]) % MOD


# Read input
N = int(input().strip())
S = input().strip()

# Print the result
print(count_distinct_strings(N, S))
