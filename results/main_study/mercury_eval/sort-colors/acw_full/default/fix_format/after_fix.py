class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		last_zero = -1
		first_two = n
		i = 0
		while i < first_two:
			if nums[i] == 0:
				last_zero += 1
				nums[i], nums[last_zero] = nums[last_zero], nums[i]
				i += 1
			elif nums[i] == 2:
				first_two -= 1
				nums[i], nums[first_two] = nums[first_two], nums[i]
			else:
				i += 1
