# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, target, result, current):
        if root == None:
            return
        current.append(root.val)
        if root.left == None and root.right == None and target == root.val:
            result.append(current.copy())
        self.helper(root.left, target - root.val, result, current)
        self.helper(root.right, target - root.val, result, current)
        current.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        current = []
        self.helper(root, targetSum, result, current)
        return result
