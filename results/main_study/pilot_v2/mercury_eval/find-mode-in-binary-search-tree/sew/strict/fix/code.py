# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class  Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        pre, cnt, max_cnt, mode=None, 0, 0, list()
        stack = []
        node = root
        while  stack or  node:
            while  node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            if not node.val != pre:
                cnt += 1
            else:
                cnt = 1
            pre=node.val
            if  cnt > max_cnt:
                max_cnt, mode = cnt, [node.val]
            elif  cnt == max_cnt:
                mode.append(node.val)
            node=node.right
        return mode
