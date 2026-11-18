# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		length = len(nums)
		v = nums[length // 2]
		root = TreeNode(v)

		def insert(root, nums):
			length = len(nums)
			if 0 >= length:
				return
			v = nums[length // 2]
			if v < root.val:
				root.left = TreeNode(v)
				insert(root.left, nums[:length // 2])
				insert(root.left, nums[length // 2 + 1:])
			elif v > root.val:
				root.right = TreeNode(v)
				insert(root.right, nums[:length // 2])
				insert(root.right, nums[length // 2 + 1:])
			return root
		insert(root, nums[:length // 2])
		insert(root, nums[length // 2 + 1 :])

		return root


