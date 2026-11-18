class Solution:
	def findMedianOfSortedArray(self, array: List[int]) -> float:
		length = len(array)
		if length % 2 != 0:
			return array[length // 2]
		else:
			return (array[length // 2] + array[(length - 1) // 2]) / 2

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if not nums1:
			return self.findMedianOfSortedArray(nums2)
		elif not nums2:
			return self.findMedianOfSortedArray(nums1)
		else:
			nums1.extend(i for i in nums2)
			nums1.sort()
			return self.findMedianOfSortedArray(nums1)
