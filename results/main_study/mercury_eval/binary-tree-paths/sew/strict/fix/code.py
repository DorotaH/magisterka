# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        ans = []

        def path(head,res,ans):
            if  head is  None:
                return None

            res.append(head.val)

            if  head.left is  None and  head.right is  None:
                ans.append(res[:])
                return None

            if  head.left:
                path(head.left,res,ans)
                res.pop()

            if  head.right:
                path(head.right,res,ans)
                res.pop()

            return

        path(root,res,ans)

        output = ["->".join(str(i) for i in lists) for lists in ans]
        return output
