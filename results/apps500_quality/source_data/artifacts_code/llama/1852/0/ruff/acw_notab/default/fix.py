import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = 2**n - 1
graph = [[] for _ in range(m)]
for _ in range(m - 2):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


def dfs(v, p):
    depth = 0
    parent = [-1] * m
    queue = deque([v])
    while queue:
        u = queue.popleft()
        for w in graph[u]:
            if w != p:
                parent[w] = u
                queue.append(w)
        depth = max(depth, len(graph[u]))
    return depth, parent


depth1, parent1 = dfs(0, -1)
depth2, parent2 = dfs(m - 1, -1)

if depth1 == depth2:
    if m % 2:
        print(0)
        sys.exit(0)
    if parent1[0] == -1 or parent2[m - 1] == -1:
        print(0)
        sys.exit(0)
    removed = m - 1 - parent2[m - 1]
    children = [i for i in range(m) if parent1[i] == removed]
    if len(children) != 2:
        print(0)
        sys.exit(0)
    print(1)
    print(removed + 1)
else:
    print(0)
