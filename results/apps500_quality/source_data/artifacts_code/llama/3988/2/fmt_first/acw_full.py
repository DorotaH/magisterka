from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def solve():
	n, m, s = map(int, input().split())
	adj = [[] for _ in range(1 + n)]
	graph = defaultdict(list)
	for _ in range(m):
		t, u, v = map(int, input().split())
		if t == 1:
			adj[u].append(v)
		else:
			graph[u].append(v)
			graph[v].append(u)

	visited = [False] * (1 + n)
	order = []
	queue = deque([s])
	visited[s] = True
	while queue:
		node = queue.popleft()
		order.append(node)
		for neighbor in adj[node]:
			if not visited[neighbor]:
				visited[neighbor] = True
				queue.append(neighbor)

	size = len(order)

	forward_graph = [[] for _ in range(1 + n)]
	backward_graph = [[] for _ in range(1 + n)]

	for u in order:
		for v in graph[u]:
			if v > u:
				forward_graph[u].append(v)
			else:
				backward_graph[u].append(v)

	reachable = [0] * (1 + n)
	for node in order:
		for neighbor in forward_graph[node]:
			reachable[neighbor] += 1

	ans1 = ""
	ans2 = ""
	for _ in range(1, m):
		u, v = map(int, input().split())
		ans1 += "+" if reachable[u] < reachable[v] else "-"
		ans2 += "+" if reachable[u] > reachable[v] else "-"
	print(size)
	print(ans1)
	print(size)
	print(ans2)


solve()
