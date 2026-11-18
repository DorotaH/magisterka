class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		low, high = 0, len(nums) - 1
		while high >= low:
			mid = (high + low) // 2
			if nums[mid] == target:
				return True
			if nums[low] == nums[mid] == nums[high]:
				low += 1
				high -= 1
			# left half is sorted
			elif nums[mid] >= nums[low]:
				if nums[low] <= target and nums[mid] >= target:
					high = mid - 1
				else:
					low = mid + 1
			# right half is sorted
			elif nums[mid] <= nums[high]:
				if target <= nums[high] and nums[mid] <= target:
					low = mid + 1
				else:
					high = mid - 1
		return False
