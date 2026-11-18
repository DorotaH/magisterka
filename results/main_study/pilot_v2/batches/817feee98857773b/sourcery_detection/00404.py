# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # getting a sorted list would be helpful because then we can just compare the difference between 2 consecutive elements instead of comparing with every element.
        # inorder traversal would give us a sorted array in a BST.

        inorder = []

        def inorder_traversal(node):
            if node == None:
                return None
            inorder_traversal(node.left)
            inorder.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)

        # since the array is sorted, we will only take the difference of 2 consecutive elements.
        min_difference = float("inf")
        for i in range(len(inorder) - 1):
            if abs(inorder[i] - inorder[i + 1]) < min_difference:
                min_difference = abs(inorder[i] - inorder[i + 1])

        return min_difference
