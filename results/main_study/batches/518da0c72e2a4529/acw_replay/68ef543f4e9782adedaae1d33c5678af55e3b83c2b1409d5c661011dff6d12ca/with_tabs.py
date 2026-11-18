class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		n = len(matrix)
		m = len(matrix[0])

		for i in range(n):
			for j in range(m):
				matrix[i][j] = int(matrix[i][j])

		ans = 0
		for i in range(n):
			dp = []
			for k in range(i, -1, -1):
				if not dp or dp[-1] == 1:
					dp.append(matrix[k][0])
					if dp[-1] == 1:
						ans = max(ans, i - k + 1)
				else:
					dp.append(0)
			dp.reverse()
			for j in range(1, m):
				valid = True
				for k in range(i, -1, -1):
					if matrix[k][j] == 0:
						valid = False

					if valid:
						ans = max(ans, (dp[k] + 1) * (i - k + 1))
						dp[k] = dp[k] + 1
					else:
						dp[k] = 0
		return ans


