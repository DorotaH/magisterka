class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		if (len(nums) == 1):
			return nums[0]
		if not nums:
			return 0
		currsum = 0
		maxsum = float('-inf')
		for i in nums:
			currsum += i
			maxsum = max(maxsum, currsum)
			currsum = max(currsum, 0)

		return maxsum
