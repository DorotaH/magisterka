import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        r = []
        l = []
        q.put(root)
        qLen = q.qsize()
        while q.qsize() != 0:
            qLen = q.qsize()
            l = []
            for _ in range(qLen):
                node = q.get()
                if node:
                    l.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if l:
                r.append(l)

        return r
