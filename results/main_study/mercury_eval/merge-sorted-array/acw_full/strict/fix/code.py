class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""

		index1 = m - 1
		index2 = n - 1
		cont = m + n - 1

		while index2 >= 0:

			value1 = nums1[index1]
			value2 = nums2[index2]

			print(str(value1) + str(value2))

			if index1 >= 0 and value1 >= value2:
				nums1[cont] = value1
				index1 -= 1

			else:
				nums1[cont] = value2
				index2 -= 1
			cont -= 1
