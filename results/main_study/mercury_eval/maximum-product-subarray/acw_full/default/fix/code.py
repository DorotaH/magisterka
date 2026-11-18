class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		prod = 1
		maxprod = 0
		maxprod2 = 0
		for i in nums:
			prod = i  * prod
			maxprod = max(maxprod, prod)
			if prod == 0:
				prod = 1
		prod = 1
		for i in range(len(nums) - 1, -1, -1):
			prod = nums[i]  * prod
			maxprod2 = max(maxprod2, prod)
			if prod == 0:
				prod = 1
		return max(maxprod, maxprod2)
