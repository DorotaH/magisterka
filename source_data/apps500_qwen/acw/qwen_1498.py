from collections import defaultdict, deque


def solve(n, m, edges, queries):
	# Build the tree
	tree = defaultdict(list)
	for u, v in edges:
		tree[u].append(v)
		tree[v].append(u)
	
	# Function to check if there is a path from root to any vertex u such that each of the given k vertices is either belongs to this path or has the distance 1 to some vertex of this path
	def has_valid_path(k, vertices):
		# Create a set of vertices for quick lookup
		vertices_set = set(vertices)
		# Initialize visited set
		visited = set()
		# Initialize queue for BFS
		queue = deque([1])
		visited.add(1)
		
		while queue:
			current = queue.popleft()
			# If the current vertex is in the set of vertices, we found a valid path
			if current in vertices_set:
				return True
			# Add all neighbors that are not visited
			for neighbor in tree[current]:
				if neighbor not in visited:
					visited.add(neighbor)
					queue.append(neighbor)
		
		# If we finish the BFS without finding a valid path, return False
		return False
	
	# Process each query
	answers = []
	for k, vertices in queries:
		if has_valid_path(k, vertices):
			answers.append("YES")
		else:
			answers.append("NO")
	
	return answers


# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Solve and print the results
results = solve(n, m, edges, queries)
for result in results:
	print(result)
