# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# Complexity Analysis
# Time complexity : O(NlogN)
# Space complexity : O(1)
class Solution:
	def countNodes(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0

		def depthOfLeft(node):
			level = 0
			while node:
				level += 1
				node = node.left
			return level

		def depthOfRight(node):
			level = 0
			while node:
				level += 1
				node = node.right
			return level

		leftLevel = depthOfLeft(root.left)
		rightLevel = depthOfRight(root.right)

		if leftLevel == rightLevel:
			return 2 ** (1 + leftLevel) - 1
		else:
			return self.countNodes(root.left) + 1 + self.countNodes(root.right)
