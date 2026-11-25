def longest_uncommon_subsequence(a, b):
	def longest_common_subsequence(a, b):
		m, n = len(a), len(b)
		dp = [[0] * (1 + n) for _ in range(1 + m)]
		for i in range(1, 1 + m):
			for j in range(1, 1 + n):
				if a[i - 1] == b[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		return dp[m][n]

	lcs = longest_common_subsequence(a, b)
	return max(len(a), len(b)) - lcs if lcs < min(len(a), len(b)) else -1


a = input()
b = input()
print(longest_uncommon_subsequence(a, b))
