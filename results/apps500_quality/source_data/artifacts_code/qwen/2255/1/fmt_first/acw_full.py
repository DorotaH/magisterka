import sys
from collections import deque


def main():
	input = sys.stdin.read
	data = input().split()

	index = 0
	n = int(data[index])
	m = int(data[1 + index])
	index += 2

	graph = [[] for _ in range(1 + n)]
	for _ in range(m):
		u = int(data[index])
		v = int(data[1 + index])
		graph[u].append(v)
		graph[v].append(u)
		index += 2

	visited = [False] * (1 + n)
	result = []

	def dfs(node):
		visited[node] = True
		result.append(node)
		for neighbor in sorted(graph[node]):
			if not visited[neighbor]:
				dfs(neighbor)

	dfs(1)

	for node in result:
		print(node, end=" ")


if __name__ == "__main__":
	main()
