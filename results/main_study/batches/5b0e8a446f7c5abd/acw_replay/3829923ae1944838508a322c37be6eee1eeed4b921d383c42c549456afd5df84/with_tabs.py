class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		l = 0
		r = len(nums) - 1
		while l <= r:
			mid = int((l + r) / 2)
			if target == nums[mid]:
				return mid
			elif nums[mid] > target:
				r = mid - 1
			elif nums[mid] < target:
				l = mid + 1
		print(mid)
		if nums[mid] > target:
			return 0 if (mid == 0) else mid
		if nums[mid] < target:
			return mid + 1
			if mid == len(nums) - 1:
				return mid + 1
			return mid if (mid == 0) else mid + 1
