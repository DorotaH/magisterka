MOD = 998244353


def count_independent_sets(n, edges):
	from collections import defaultdict

	# Build the adjacency list for the tree
	adj = defaultdict(list)
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)

	# Function to count independent sets in a subtree rooted at node 1
	def dfs(node, parent):
		if len(adj[node]) == 1 and adj[node][0] == parent:
			return 2  # Only the node itself and the empty set

		total = 1  # Count the empty set
		for neighbor in adj[node]:
			if neighbor != parent:
				total += dfs(neighbor, node)
				total %= MOD

		# Count the sets that include the node
		include_node = 0
		for neighbor in adj[node]:
			if neighbor != parent:
				include_node += dfs(neighbor, node)
				for sub in range(include_node):
					total += 1
					total %= MOD

		return total

	return (dfs(1, -1) - 1) % MOD  # Subtract the empty set


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
edges = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(n - 1)]

# Calculate and print the result
result = count_independent_sets(n, edges)
print(result)
