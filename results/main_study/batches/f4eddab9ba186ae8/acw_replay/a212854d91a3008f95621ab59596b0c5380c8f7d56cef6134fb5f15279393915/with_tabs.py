# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		tree1 = []
		tree2 = []
		tree11 = []
		tree22 = []

		def inorderTrasverse(head, arr):

			if head:
				inorderTrasverse(head.left, arr)
				arr.append(head.val)
				inorderTrasverse(head.right, arr)

		def preorderTrasverse(head, arr):

			if head:
				arr.append(head.val)
				preorderTrasverse(head.left, arr)
				preorderTrasverse(head.right, arr)
			else:
				arr.append('dhruv')


		inorderTrasverse(p, tree1)
		inorderTrasverse(q, tree2)
		preorderTrasverse(p, tree11)
		preorderTrasverse(q, tree22)
		print(tree1, tree2)
		return (tree1 == tree2) and (tree11 == tree22)



