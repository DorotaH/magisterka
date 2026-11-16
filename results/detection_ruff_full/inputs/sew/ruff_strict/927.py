class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_height(node):
    if node is not None:
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        if left_height > right_height:
            return left_height + 1
        return right_height + 1
    return 0
