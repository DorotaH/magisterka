import sys
from collections import defaultdict, deque


def bfs(root, n, graph):
	visited = [False] * (1 + n)
	visited[root] = True
	queue = deque([root])
	distance = [0] * (1 + n)
	parent = [-1] * (1 + n)
	while queue:
		current = queue.popleft()
		for neighbor in graph[current]:
			if not visited[neighbor]:
				visited[neighbor] = True
				queue.append(neighbor)
				distance[neighbor] = 1 + distance[current]
				parent[neighbor] = current
	return distance, parent


def find_path(distance, parent, target, root):
	path = []
	while target != root:
		path.append(target)
		target = parent[target]
	path.append(root)
	path.reverse()
	return path


def solve(n, m, edges, queries):
	graph = defaultdict(list)
	for u, v in edges:
		graph[u].append(v)
		graph[v].append(u)

	distance, parent = bfs(1, n, graph)

	results = []
	for k, *vertices in queries:
		covered = set()
		for v in vertices:
			if v in covered:
				continue
			path = find_path(distance, parent, v, 1)
			covered.update(path)
			for u in path:
				if distance[u] == 1:
					covered.update(graph[u])

		if len(covered) == len(vertices):
			results.append("YES")
		else:
			results.append("NO")

	return results


# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
edges = []
index = 2
for _ in range(n - 1):
	u = int(data[index])
	v = int(data[1 + index])
	edges.append((u, v))
	index += 2

queries = []
for _ in range(m):
	k = int(data[index])
	vertices = list(map(int, data[1 + index : 1 + index + k]))
	queries.append((k, *vertices))
	index += k + 1

# Solve and print results
results = solve(n, m, edges, queries)
for result in results:
	print(result)
