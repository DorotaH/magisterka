# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:
    def  minDepth(self, root: Optional[TreeNode]) -> int:
        if  not  root:
            return  0
        q = [root]
        depth = 0
        found = False
        while  q and  not  found:
            depth += 1
            for  _ in  range(len(q)):
                first = q.pop(0)
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                if not first.left and not first.right:
                    found=True
        return depth
