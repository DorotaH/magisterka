class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		nums = nums + [1] + [1]
		dp = {}

		def dfs(l, r):
			if l > r:
				return 0
			if (l, r) in dp:
				return dp[(l, r)]
			total = 0
			for j in range(l, 1 + r):
				total = max(
					total,
					dfs(l, j - 1) + dfs(1 + j, r) + nums[l - 1] * nums[1 + r] * nums[j],
				)
			dp[(l, r)] = total
			return dp[(l, r)]

		return dfs(1, len(nums) - 2)
