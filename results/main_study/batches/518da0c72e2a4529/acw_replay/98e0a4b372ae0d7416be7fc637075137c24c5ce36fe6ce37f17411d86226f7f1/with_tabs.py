class Solution:
	def printsubsets(self, n, nums, l1, index, a):
		if (index == n):
			a.append(l1.copy())
			return
		l1.append(nums[index])
		self.printsubsets(n, nums, l1, 1 + index, a)
		l1.remove(nums[index])
		self.printsubsets(n, nums, l1, 1 + index, a)

	def subsets(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		l1 = []
		index = 0
		a = []
		self.printsubsets(n, nums, l1, index, a)
		return a
