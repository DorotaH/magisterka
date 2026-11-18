# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        invalid = []
        prev = {}
        self.visitTree(root, prev, invalid)

        print(len(invalid))

        # swap invalid values
        larger = invalid[0].val
        smaller = invalid[1].val

        invalid[0].val = smaller
        invalid[1].val = larger
    
    def visitTree(self, root, prev, invalid: List[TreeNode]):
        if root is None:
            return

        if len(invalid) == 3:
            return

        self.visitTree(root.left, prev, invalid)

        if prev and prev["ptr"].val > root.val:
            if not invalid:
                invalid.append(prev["ptr"])
                invalid.append(root)
            elif len(invalid) < 3:
                invalid[1] = root
                invalid.append(None)

        prev["ptr"] = root

        self.visitTree(root.right, prev, invalid)