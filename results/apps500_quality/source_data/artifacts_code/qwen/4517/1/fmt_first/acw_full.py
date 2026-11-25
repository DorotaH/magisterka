from collections import defaultdict, deque


def find_path_to_vertex(graph, root, target):
	queue = deque([root])
	parent = {root: None}
	while queue:
		node = queue.popleft()
		if node == target:
			path = []
			while node is not None:
				path.append(node)
				node = parent[node]
			return path[::-1]
		for neighbor in graph[node]:
			if neighbor not in parent:
				parent[neighbor] = node
				queue.append(neighbor)
	return None


def is_valid_path(graph, root, query):
	vertices = set(query)
	path = find_path_to_vertex(
		graph, root, max(vertices, key=lambda v: len(vertices & set(graph[v])))
	)
	if not path:
		return False
	return not any(
		vertex not in path and all(abs(vertex - p) != 1 for p in path)
		for vertex in vertices
	)


def main():
	import sys

	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	m = int(data[1])
	edges = data[2 : 2 * n - 1]
	queries = data[2 * n - 1 :]

	graph = defaultdict(list)
	index = 2
	for _ in range(n - 1):
		u = int(edges[index]) - 1
		v = int(edges[1 + index]) - 1
		graph[u].append(v)
		graph[v].append(u)
		index += 2

	results = []
	for i in range(m):
		k = int(queries[i * 2]) - 1
		query = list(map(int, queries[i * 2 + 1 : i * 2 + 1 + k]))
		results.append("YES" if is_valid_path(graph, 0, query) else "NO")

	print("\n".join(results))


if __name__ == "__main__":
	main()
