from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(0, N + 1)]
for _ in range(0, M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
S, T = map(int, input().split())

queue = deque([(S, 0)])
visited = {S}
while queue:
    node, dist = queue.popleft()
    if T == node:
        print(dist)
        exit(0)
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, dist + 1))

print(0)
