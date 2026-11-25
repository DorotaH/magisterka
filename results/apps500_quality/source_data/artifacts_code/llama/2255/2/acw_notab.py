from collections import deque
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(1 + n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node, parent, depth, visited, ans, order):
    visited[node] = True
    for neighbor in graph[node]:
        if neighbor != parent:
            if not visited[neighbor]:
                dfs(neighbor, node, depth + 1, visited, ans, order)
            elif depth > visited[neighbor]:
                order.append((depth, neighbor))


visited = [False] * (1 + n)
order = []
for i in range(1, 1 + n):
    if not visited[i]:
        dfs(i, i, 0, visited, order, order)

order.sort()
for i in range(1, n):
    if order[i][1] < order[i - 1][1]:
        print(' '.join(map(str, [order[j][1] for j in range(i)])), end=' ')
        for j in range(i, n):
            print(order[j][1], end=' ')
        break
else:
    print(' '.join(map(str, [order[i][1] for i in range(n)])))
