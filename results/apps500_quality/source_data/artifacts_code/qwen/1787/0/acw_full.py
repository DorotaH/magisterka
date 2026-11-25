MOD = 7 + 10**9


def count_sequences(s):
	n = len(s)
	a_positions = []
	b_positions = []
	for i in range(n):
		if s[i] == 'a':
			a_positions.append(i)
		elif s[i] == 'b':
			b_positions.append(i)

	m = len(a_positions)
	k = len(b_positions)

	# Initialize DP table
	dp = [[0] * (k + 1) for _ in range(1 + m)]
	dp[0][0] = 1

	# Fill the DP table
	for i in range(1, 1 + m):
		dp[i][0] = dp[i - 1][0]
		for j in range(1, 1 + min(i, k)):
			dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

	return dp[m][k]


# Read input
import sys
input = sys.stdin.read
data = input().split()
s = data[0]

# Print the result
print(count_sequences(s))
