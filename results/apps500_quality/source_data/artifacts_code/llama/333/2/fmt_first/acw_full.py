a = input().strip()
b = input().strip()


def longest_uncommon_subsequence(a, b):
	def lcs_length(a, b):
		m, n = len(a), len(b)
		dp = [[0] * (1 + n) for _ in range(1 + m)]

		for i in range(1 + m):
			for j in range(1 + n):
				if i == 0 or j == 0:
					dp[i][j] = 0
				elif a[i - 1] == b[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

		return dp[m][n]

	lcs_ab = lcs_length(a, b)
	lcs_ba = lcs_length(b, a)

	if lcs_ab == lcs_ba and lcs_ab == max(len(a), len(b)):
		return -1
	else:
		return max(len(a), len(b))


print(longest_uncommon_subsequence(a, b))
