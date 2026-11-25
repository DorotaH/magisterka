import sys

input = sys.stdin.readline

from  collections import  deque
from  functools import  lru_cache
from  collections import  defaultdict

def dfs(node, parent, tree):
    size = 1
    for  child in  tree[node]:
        if  parent != child:
            size = size + dfs(child, node, tree)
    return size

def solve():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for  _ in  range(0, n - 1):
        u, v=map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    max_distance = 0
    leaves = set()

    @lru_cache(maxsize=None)
    def get_distance(u, v):
        if  u == v:
            return 0
        return (
            dfs(u, -1, tree)
            + dfs(v, -1, tree)
            - (2 * dfs(u, -1, tree))
            - (2 * dfs(v, -1, tree))
        )

    @lru_cache(maxsize=None)
    def get_max_distance(u, v):
        leaves.add(u)
        leaves.add(v)
        return max_distance + get_distance(u, v)

    @lru_cache(maxsize=None)
    def get_max_distance_for_leaves(u):
        return max_distance + get_distance(u, next(iter(leaves - {u})))

    queue = deque(
        [
            (i, get_max_distance_for_leaves(i))
            for i in range(1, n + 1)
            if len(tree[i]) == 1
        ]
    )
    max_distance = 0
    result = []
    while queue:
        node, distance=queue.popleft()
        max_distance=max(max_distance, distance)
        result.append((node, next(iter(leaves)), next(iter(leaves)), node))
        leaves.remove(node)
        for child in tree[node]:
            if  child != -1 and  1 == len(tree[child]):
                queue.append((child, get_max_distance_for_leaves(child)))
            elif  child != -1:
                tree[child].remove(node)
                tree[node].remove(child)

    print(max_distance)
    for  node, u, v, c in  result[::-1]:
        print(u, v, c)


solve()
