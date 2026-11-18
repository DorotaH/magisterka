# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # recursive DFS
        # if root.left is None and root.right is None:
        #     return 1
        # if root.left is None:
        #     return 1+max(1, self.maxDepth(root.right))
        # if root.right is None:
        #     return 1+max(1, self.maxDepth(root.left))
        # return 1+max(self.maxDepth(root.right), self.maxDepth(root.left))

        # BFS with queue
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level