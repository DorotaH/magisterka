from collections import deque

N, M = map(int, input().split())
graph = {}
for _ in range(M):
	u, v = map(int, input().split())
	if u not in graph:
		graph[u] = []
	if v not in graph:
		graph[v] = []
	graph[u].append(v)

queue = deque()
for node in graph:
	if len(graph[node]) == 1:
		queue.append(node)

ans = []
while queue:
	node = queue.popleft()
	ans.append(node)
	for neighbor in graph:
		if node in graph[neighbor]:
			graph[neighbor].remove(node)
			if len(graph[neighbor]) == 1:
				queue.append(neighbor)

if len(ans) != N:
	print(-1)
else:
	print(len(ans))
	print('\n'.join(map(str, ans)))
