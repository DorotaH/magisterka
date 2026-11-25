def is_bridge(graph, u, v):
	def dfs(node, visited, parent):
		visited[node] = True
		for neighbor in graph[node]:
			if not visited[neighbor]:
				if dfs(neighbor, visited, node):
					return True
			elif neighbor != parent:
				return True
		return False

	visited = [False] * len(graph)
	return not dfs(u, visited, -1)


def build_k_regular_graph(k):
	if k == 1:
		return "NO"

	n = 2 * k
	graph = [[] for _ in range(n)]

	# Create a cycle
	for i in range(n):
		graph[i].append((i + 1) % n)
		graph[(i + 1) % n].append(i)

	# Add a bridge
	bridge_u, bridge_v = 0, n - 1
	graph[bridge_u].append(bridge_v)
	graph[bridge_v].append(bridge_u)

	return f"YES\n{n} {n - 1}\n{1 + bridge_u}\n"


# Read input
k = int(input().strip())

# Build and print the graph
result = build_k_regular_graph(k)
print(result)
