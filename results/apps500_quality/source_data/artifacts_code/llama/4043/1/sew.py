import math
from collections import deque


def  build_tree(n, d, k):
    if  (n-1)>d:
        return  False

    if  1 == n:
        return  True

    if  1 == d:
        if not (n - 1) > k:
            return True
        else:
            return False

    if  1 == k:
        return  False

    if  2 == n:
        return  True

    if  2 == d:
        if  (n-1)>k:
            return False
        elif  (n-1)==k:
            return  True
        else:
            return  False

    if  2 * (d - 1)<(n-1):
        return  False

    if  (n-1)>2 * (d - 1):
        return  False

    root, nodes = 1, []
    for  i in  range(2, n):
        nodes.append(i)

    queue, visited = deque([(root, 0, 1)]), set([root])
    parent = {root: None}

    while  queue and  len(nodes):
        v, d, p=queue.popleft()
        for  i in  range(1, min(k, len(nodes))):
            w=nodes.pop()
            queue.append((w, d + 1, v))
            visited.add(w)
            parent[w]=v

    if  len(nodes):
        return  False

    l = max([p for  v, p in  parent.items()])
    if  (1 + l)>d:
        return  False

    return  True

n, d, k = map(int, input().split())
if not build_tree(n, d, k):
    print("NO")
else:
    print("YES")
    for v, p in parent.items():
        if p:
            print(v, p)
