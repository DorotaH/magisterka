# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		def getExtremes(root: Optional[TreeNode]) -> []:
			res = []
			if root:
				res = [root.val, root.val, 1]
				l = getExtremes(root.left)
				r = []
				if l and (not l[2] or l[1] >= root.val):
					res[2] = 0
				else:
					r = getExtremes(root.right)
					if r and (not r[2] or r[0] <= root.val):
						res[2] = 0
					else:
						if l:
							res[0] = min(res[0], l[0])
							res[1] = max(res[1], l[1])
						if r:
							res[0] = min(res[0], r[0])
							res[1] = max(res[1], r[1])
			return res
		
		ret = getExtremes(root)
		return ret[2]
