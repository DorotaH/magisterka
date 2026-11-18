# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		if len(preorder) == 1: return TreeNode(preorder[0])
		if not preorder: return None

		root    = TreeNode(preorder[0])
		rootloc = inorder.index(preorder[0])
		nleft   = len(inorder[:rootloc])

		root.left  = self.buildTree(preorder[1:1 + nleft], inorder[:rootloc])
		root.right = self.buildTree(preorder[1 + nleft:], inorder[1 + rootloc:])

		return root


		tree;
		while preorder:
			tree = TreeNode(preorder[0])
			inordex = inorder.index(preorder[0])
			preorder.pop(0)
			tree.left = self.buildTree(preorder, )
