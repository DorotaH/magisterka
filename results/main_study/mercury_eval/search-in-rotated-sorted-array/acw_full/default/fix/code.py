class Solution:
	def search(self, nums: List[int], target: int) -> int:
		# nums length
		nums_length = len(nums)

		# set low and high
		low = 0
		high = nums_length - 1

		# initialise base index
		base_index = 0

		# search for lowest value
		while high >= low:
			# find mid
			mid = (high + low) // 2

			if mid > 0 and nums[mid] < nums[mid - 1]:
				# base index found
				base_index = mid
				break
			elif nums[-1] < nums[mid]:
				# check right
				low = mid + 1
			else:
				# check left
				high = mid - 1

		def binary_search(num_list):
			lo = 0
			hi = nums_length - 1

			while lo <= hi:
				mid = (lo + hi) // 2

				if num_list[mid] == target:
					# if target found, return index adjusted for rotation
					return (mid + base_index) % nums_length
				elif num_list[mid] < target:
					lo = mid + 1
				else:
					hi = mid - 1

			return -1

		# send stitched together derotated list to binary_search function
		return binary_search(nums[:base_index] + nums[base_index:])
