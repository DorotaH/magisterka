def mul_consecutive_nums(nums):
	return [a * b for a, b in zip(nums[:-1], nums[1:])]
