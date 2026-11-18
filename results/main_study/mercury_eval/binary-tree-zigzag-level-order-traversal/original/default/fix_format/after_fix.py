class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        rightToLeft = False

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level.append(node.val)

            if rightToLeft:
                level = level[::-1]

            rightToLeft = not rightToLeft
            res.append(level)

        return res