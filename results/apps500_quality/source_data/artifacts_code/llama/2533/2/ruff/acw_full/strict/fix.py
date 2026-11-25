from collections import deque


def dfs(graph, node, visited, stack):
	visited[node] = True
	stack.append(node)
	for neighbor in graph[node]:
		if not visited[neighbor]:
			dfs(graph, neighbor, visited, stack)


def topological_sort(graph):
	visited = [False] * len(graph)
	stack = []
	for node in range(len(graph)):
		if not visited[node]:
			dfs(graph, node, visited, stack)
	return stack[::-1]


def make_road_network_tourist_friendly(graph, edges):
	n = len(graph)
	if not graph:
		return "YES"
	cycle = False
	for i in range(n):
		if graph[i]:
			queue = deque([i])
			visited = [False] * n
			while queue:
				node = queue.popleft()
				if visited[node]:
					cycle = True
					break
				visited[node] = True
				for neighbor in graph[node]:
					queue.append(neighbor)
	if cycle:
		return "NO"
	stack = topological_sort(graph)
	result = [(stack[i], stack[(i + 1) % len(stack)]) for i in range(len(stack))]
	return "YES\n" + "\n".join(f"{a} {b}" for a, b in result)


def main():
	n, e = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(e):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
	print(make_road_network_tourist_friendly(graph, e))


if __name__ == "__main__":
	main()
