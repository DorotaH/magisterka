class Solution:
	def traverse(self, x: int, y: int, xt: int, yt: int, dp: List[List[int]]) -> int:

		if x == xt and y == yt:
			return 1
		elif xt < x or y > yt:
			return 0
		elif dp[x][y] != -1:
			return dp[x][y]
		else:
			dp[x][y] = self.traverse(1 + x, y, xt, yt, dp) + self.traverse(
				x, y + 1, xt, yt, dp
			)
			return dp[x][y]

	def uniquePaths(self, m: int, n: int) -> int:
		rx = m - 1
		ry = n - 1
		dp = [[-1 for _ in range(1 + n)] for _ in range(1 + m)]

		num = self.traverse(0, 0, rx, ry, dp)
		return num if m == 1 and n == 1 else dp[0][0]
