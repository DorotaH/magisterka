from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
S, T = map(int, input().split())

queue = deque([(S, 0)])
visited = {S}
while queue:
	node, dist = queue.popleft()
	if node == T:
		print(dist)
		exit(0)
	for neighbor in graph[node]:
		if neighbor not in visited:
			visited.add(neighbor)
			queue.append((neighbor, dist + 1))

print(0)
