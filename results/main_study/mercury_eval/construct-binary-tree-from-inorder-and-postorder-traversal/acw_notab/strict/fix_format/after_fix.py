
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None
        return self.traversal(inorder, postorder)

    def traversal(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        root_value = postorder[-1]
        root = TreeNode(root_value)

        if len(postorder) == 1:
            return root

        index = next((i for i in range(len(inorder)) if inorder[i] == root_value), 0)
        leftInorder = inorder[:index]
        rightInorder = inorder[1 + index:]

        postorder.pop()
        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):]

        root.left = self.traversal(leftInorder, leftPostorder)
        root.right = self.traversal(rightInorder, rightPostorder)
        return root
