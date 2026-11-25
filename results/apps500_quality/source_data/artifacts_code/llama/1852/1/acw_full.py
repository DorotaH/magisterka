import sys
import math
from collections import deque, defaultdict

n = int(input())
total_nodes = 2 ** n - 1
graph = [[] for _ in range(total_nodes)]
for _ in range(total_nodes - 1):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)
	graph[v - 1].append(u - 1)


def is_complete(root, parent, visited):
	if len(graph[root]) != 2 ** n - 1:
		return False
	for child in graph[root]:
		if child == parent:
			continue
		if len(graph[child]) != 2 ** (n - 1):
			return False
		if is_complete(child, root, visited):
			visited.add(child)
	return True


def dfs(root, parent, removed):
	if len(graph[root]) == 1 and root != parent:
		return root
	for child in graph[root]:
		if child != parent and len(graph[child]) == 2 ** (n - 1):
			return dfs(child, root, removed)


def main():
	root = 0
	visited = set()
	if is_complete(root, -1, visited):
		removed = dfs(root, -1, -1)
		if removed != -1:
			print(1)
			print(removed + 1)
		else:
			print(0)
	else:
		print(0)


if __name__ == "__main__":
	main()
