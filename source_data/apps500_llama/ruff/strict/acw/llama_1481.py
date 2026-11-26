import math
from collections import deque


def build_tree(n, d, k):
    if (n - 1) > d:
        return False

    if n == 1:
        return True

    if d == 1:
        return False if k < (n - 1) else True
    if k == 1:
        return False

    if n == 2:
        return True

    if d == 2:
        if k < (n - 1):
            return False
        elif (n - 1) == k:
            return True
        else:
            return False

    if 2 * (d - 1) < (n - 1):
        return False

    root = 1
    nodes = list(range(2, n))
    queue = deque([(root, 0, 1)])
    visited = set([root])
    parent = {root: None}

    while queue and len(nodes):
        v, d, p = queue.popleft()
        for _ in range(1, min(k, len(nodes))):
            w = nodes.pop()
            queue.append((w, 1 + d, v))
            visited.add(w)
            parent[w] = v

    if len(nodes):
        return False

    l = max(p for v, p in parent.items())
    if (l + 1) > d:
        return False

    return True


n, d, k = map(int, input().split())
if build_tree(n, d, k):
    print("YES")
    for v, p in parent.items():
        if p:
            print(v, p)
else:
    print("NO")
