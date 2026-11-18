# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def  inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        myStack = []
        myList = []
        while  1:
            if  node is  not None:
               myStack.append(node)
               node=node.left
            elif  len(myStack) != 0:
                myPop=myStack.pop()
                if  myPop is  None:
                    continue
                myList.append(myPop.val)
                node=myPop.right
            else:
                break
        return  myList





