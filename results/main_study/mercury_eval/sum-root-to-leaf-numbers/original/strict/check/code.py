# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        collect = []
        final = []
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        return self.helper(root, collect, final)

    def helper(self, root, collect, final):
        collect.append(root.val)
        if not root.left and not root.right:
            print('collect', collect)
            res = int("".join(map(str, collect)))
            final.append(res)
            print("final", final)
            collect.pop()
            return
        if root.left:
            self.helper(root.left, collect, final)
        if root.right:
            self.helper(root.right, collect, final)
        collect.pop()
        return sum(final)