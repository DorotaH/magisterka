# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        return self.traversal(inorder, postorder)

    def traversal(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        root_value = postorder[-1]
        root = TreeNode(root_value)

        if len(postorder) == 1:
            return root

        index = 0
        for i in range(0, len(inorder)):
            if inorder[i] == root_value:
                index = i
                break

        leftInorder, rightInorder = inorder[0:index], inorder[index + 1 :]

        postorder.pop()
        leftPostorder, rightPostorder = (
            postorder[0 : len(leftInorder)],
            postorder[len(leftInorder) :],
        )

        root.left = self.traversal(leftInorder, leftPostorder)
        root.right = self.traversal(rightInorder, rightPostorder)
        return root
