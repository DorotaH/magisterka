# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.res = []
#         def dfs(node):
#             if node is None:
#                 return None
#             dfs(node.left)
#             dfs(node.right)
#             self.res.append(node.val)
#             return self.res
#         return dfs(root)

        # res = []
        # def dfs(node):
        #     if not node:return None
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        # dfs(root)
        # return res

### Iterative better solution

        # res = []
        # stack = []
        # stack.append((root,False))
        # while stack:
        #     node,flag = stack.pop()
        #     if node:
        #         if flag:
        #             res.append(node.val)
        #         else:
        #             stack.append((node,True))
        #             stack.append((node.right,False))
        #             stack.append((node.left,False))
        # return res

        res = []
        stack = [(root, False)]
        while stack:
            node,flag = stack.pop()
            if node:
                if flag:
                    res.append(node.val)
                else:
                    stack.append((node,True))
                    if node.right:
                        stack.append((node.right,False))
                    if node.left:
                        stack.append((node.left,False))
        return res
