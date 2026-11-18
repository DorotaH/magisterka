# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:

    def target(self, root, targetSum, s):
        a=b=c=d=False
        if(root is  None):
            a = False
            return False
        if(root.left is  None and  root.right is  None and  s + root.val == targetSum):
            b = True
            if(b==True):
                return True
        if(root.left is  not None):
            c = self.target(root.left,targetSum,s + root.val)
            if(c==True):
                return True
        if(root.right is  not None):
            d = self.target(root.right,targetSum,s + root.val)
            if(d==True):
                return True
        return  a or  b or  c or  d

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root is  None):
            return False
        s=root.val
        if(s==targetSum and  root.left is  None and  root.right is  None):
            return True
        d=self.target(root.left,targetSum,s)
        if(d == True):
            return True
        d=self.target(root.right,targetSum,s)
        return  d
