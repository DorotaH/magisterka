# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(left,right):
            if  not  left and  not  right:
                return  True
            if  not  left or  not  right:
                return  False
            return  (right.val == left.val) and  ismirror(left.left, right.right) and  ismirror(left.right, right.left)

        if not root:
            return  True
        return  ismirror(root.left, root.right)

        if not root:
            return  True

        queue = deque([(root.left, root.right)])

        while  queue:

            left, right=queue.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return  False
            if right.val != left.val:
                return  False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return  True



        