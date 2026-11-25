from collections import deque

N, M = map(int, input().split())
G = [list() for _ in range(0, N + 1)]
for _ in range(0, M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

S, T = map(int, input().split())
visited = [0] * (N + 1)
distance = [float("inf")] * (N + 1)
distance[S] = 0

queue = deque([S])
while queue:
    u = queue.popleft()
    if visited[u]:
        continue
    visited[u] = 1
    for v in G[u]:
        if distance[v] == float("inf"):
            distance[v] = distance[u] + 1
            queue.append(v)

print(distance[T] if distance[T] != float("inf") else 0)
