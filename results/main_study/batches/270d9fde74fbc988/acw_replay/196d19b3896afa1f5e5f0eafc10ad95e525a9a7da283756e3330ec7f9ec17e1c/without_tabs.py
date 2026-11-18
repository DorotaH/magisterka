class Solution:
	def maximalRectangle(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix or not matrix[0]:
			return 0
		n = len(matrix[0])
		height = [0] * (1 + n)
		ans = 0
		for row in matrix:
			for i in range(n):
				height[i] = height[i] + 1 if row[i] == '1' else 0
			stack = [-1]
			for i in range(1 + n):
				while height[i] < height[stack[-1]]:
					h = height[stack.pop()]
					w = i - 1 - stack[-1]
					ans = max(ans, h * w)
				stack.append(i)
		return ans
