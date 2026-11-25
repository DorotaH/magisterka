import sys
from collections import deque
from math import sqrt


def bfs_tree(adj):
    parent = [0] * (1 + len(adj))
    queue = deque([(1, -1)]
    )
    while queue:
        node, par = queue.popleft()
        for nei in adj[node]:
            if nei != par:
                parent[nei] = node
                queue.append((nei, node))
    return parent


def compute_distance(parent, node):
    distance = [0] * (len(parent))
    queue = deque([(node, 0)])
    while queue:
        curr_node, d = queue.popleft()
        distance[curr_node] = d
        for nei in adj[curr_node]:
            if parent[nei] == curr_node:
                queue.append((nei, 1 + d))
    return distance


def get_min_distance(adj):
    distance = [0] * (1 + len(adj))
    for i in range(1, len(adj)):
        distance[i] = max(distance[i], compute_distance(adj, i)[i] + distance[adj[i]])
    return distance


n = int(sys.stdin.readline())
adj = [[] for _ in range(1 + n)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

parent = bfs_tree(adj)
distance = get_min_distance(adj)

ans = 0
operations = []
for i in range(2, 1 + n):
    if len(adj[i]) == 1:
        ans += distance[i]
        if i != n:
            operations.append((parent[i], i, i))

print(ans)
for u, v, removed in operations:
    print(f"{u} {v} {removed}")
