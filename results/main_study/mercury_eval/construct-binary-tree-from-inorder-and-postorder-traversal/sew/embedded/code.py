from typing import List, Optional

# Definition for a binary tree node.
class  TreeNode:
    def  __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class  Solution:
    def  buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if 0 == len(inorder) or 0 == len(postorder):
            return  None
        return self.traversal(inorder, postorder)

    def  traversal(self, inorder, postorder):
        if 0 == len(inorder):
            return  None

        root_value=postorder[-1]
        root=TreeNode(root_value)

        if 1 == len(postorder):
            return  root

        index=0
        for  i in  range(0, len(inorder)):
            if inorder[i] == root_value:
                index=i
                break

        leftInorder, rightInorder = inorder[0:index], inorder[index + 1:]

        postorder.pop()
        leftPostorder, rightPostorder = postorder[0:len(leftInorder)], postorder[len(leftInorder):]

        root.left=self.traversal(leftInorder, leftPostorder)
        root.right=self.traversal(rightInorder, rightPostorder)
        return root
