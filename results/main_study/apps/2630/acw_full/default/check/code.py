class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		m = len(obstacleGrid) #row
		n = len(obstacleGrid[0]) #col
		path = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m):
			if obstacleGrid[i][0] == 0:
				path[i][0] = 1
			else:
				break
		for i in range(n):
			if obstacleGrid[0][i] == 0:
				path[0][i] = 1
			else:
				break
		for i in range(1, m):
			for j in range(1, n):
					path[i][j] = path[i][j - 1] + path[i - 1][j] if obstacleGrid[i][j] != 1 else 0
		return path[m - 1][n - 1]
