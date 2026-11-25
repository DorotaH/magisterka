from collections import deque

N, M = map(int, input().split())
G = [list() for  _ in  range(N + 1)]
for  _ in  range(M):
    a, b=map(int, input().split())
    G[a].append(b)
    G[b].append(a)

S, T = map(int, input().split())

dist = [-1] * (N + 1)
dist[S] = 0

queue = deque([S])

while queue:
    u=queue.popleft()
    for v in G[u]:
        if dist[v]==-1:
            queue.append(v)
            dist[v]=dist[u] + 1

if not dist[T] != -1:
    print(0)
else:
    print(dist[T])
