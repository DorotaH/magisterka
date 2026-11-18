# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:
    def  isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def getHeight(root):
            if not root: return 0

            leftHeight = getHeight(root.left) 
            rightHeight = getHeight(root.right)
            print(leftHeight, rightHeight)
            if(leftHeight == -1 or rightHeight == -1): 
                return min(leftHeight, rightHeight)
            if(abs(leftHeight - rightHeight) > 1): 
                print('here')
                return -1
            return  max(1+leftHeight, 1+rightHeight)
        return  getHeight(root)!=-1



        
