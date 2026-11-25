from collections import deque


def dijkstra(graph, start):
	distances = {i: [float('inf')] * k for i in range(1, k + 1)}
	distances[start][start] = 0
	queue = deque([start])
	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			cost = graph[node][neighbor] + distances[node][node]
			if cost < distances[neighbor][neighbor]:
				distances[neighbor] = k * [cost]
				queue.append(neighbor)
	return distances


n, m, k = map(int, input().split())
c = list(map(int, input().split()))
graph = {i: {} for i in range(1, 1 + n)}
for _ in range(m):
	u, v, x = map(int, input().split())
	u, v = min(u, v), max(u, v)
	graph[u][v] = min(graph.get(v, float('inf')), x)
	graph[v][u] = min(graph.get(u, float('inf')), x)

for i in range(k):
	if c[i] == 1:
		for j in range(1, 1 + n):
			if j >= c[i - 1] + 1 and c[i] >= j:
				graph[j][j] = 0

for i in range(1, k):
	if c[i] == 1:
		for j in range(1, 1 + n):
			if j >= c[i - 1] + 1 and c[i] >= j:
				for l in range(1, 1 + n):
					if l >= c[i] + 1 and l <= c[i + 1]:
						graph[j][l] = 0
						graph[l][j] = 0

d = []
for i in range(1, k + 1):
	try:
		d.append(dijkstra(graph, i)[i])
	except KeyError:
		d.append([-1] * k)

if -1 in d[0]:
	print('No')
else:
	print('Yes')
	for row in d:
		print(*row)
