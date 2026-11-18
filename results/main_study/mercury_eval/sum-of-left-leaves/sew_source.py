# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:
    def  sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def  traverse(node: Optional[TreeNode], isLeft: bool):
            if  node.left:
                traverse(node.left, True)
                if node.right:
                    traverse(node.right, False)
            elif  node.right:
                traverse(node.right, False)
            elif  isLeft:
                nonlocal  res
                res += node.val
        
        res=0
        traverse(root, False)
        return res