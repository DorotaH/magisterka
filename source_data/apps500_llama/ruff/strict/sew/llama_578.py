N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for _ in range(0, M):
    u, v = map(int, input().split())
    graph[u].append(1 + _)
    graph[v].append(1 + _)

for i in range(1, 1 + N):
    print(len(graph[i]))
