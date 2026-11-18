# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# Using a list as a stack to store current items
		# Travesal the root and handle middle item first
		# Push right nodes into stack first so that it will be populated after left
		# Use another list to store results
		if not root:
			return []
		result = []
		stack = [root]
		while stack:
			node = stack.pop()
			result.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return result

	def preorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []

		left = self.preorderTraversal(root.left)
		right = self.preorderTraversal(root.right)

		return [root.val] + left + right
