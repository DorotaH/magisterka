class Solution:
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if nums == []:
			return []

		dct = {}
		for el in nums:
			if el in dct:
				dct[el] += 1
			else:
				dct[el] = 1

		return [key for key, value in dct.items() if value > len(nums) // 3]

