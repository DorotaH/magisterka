N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(_ + 1)
	graph[v].append(_ + 1)

for i in range(1, N + 1):
	print(len(graph[i]))
