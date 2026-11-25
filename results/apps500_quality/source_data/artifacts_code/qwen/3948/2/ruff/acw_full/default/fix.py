from collections import defaultdict, deque


def is_k_multihedgehog(n, k, edges):
	# Create adjacency list for the graph
	adj = defaultdict(list)
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)

	center = next((u for u in range(1, 1 + n) if 3 <= len(adj[u])), None)
	if center is None:
		return "No"

	# Check if all other vertices have degree 1
	for u in range(1, 1 + n):
		if u != center and len(adj[u]) != 1:
			return "No"

	# Check the structure of the k-multihedgehog
	queue = deque([center])
	visited = set([center])

	while queue:
		current = queue.popleft()
		for neighbor in adj[current]:
			if neighbor in visited:
				continue
			visited.add(neighbor)
			if len(adj[neighbor]) != 2:
				return "No"
			queue.append(neighbor)

	return "Yes"


# Read input
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output result
print(is_k_multihedgehog(n, k, edges))
