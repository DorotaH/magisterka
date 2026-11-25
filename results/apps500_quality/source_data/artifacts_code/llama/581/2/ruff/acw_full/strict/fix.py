import sys

input = sys.stdin.readline

from collections import deque
from functools import cache


def dfs(node, parent, tree):
	return sum(
		dfs(child, node, tree) for child in tree[node] if child != parent
	) + 1


def solve():
	n = int(input())
	tree = [[] for _ in range(1 + n)]
	for _ in range(n - 1):
		u, v = map(int, input().split())
		tree[u].append(v)
		tree[v].append(u)

	max_distance = 0
	leaves = set()

	@cache
	def get_distance(u, v):
		if u == v:
			return 0
		return dfs(v, -1, tree) + dfs(u, -1, tree) - 2 * dfs(u, -1, tree) - dfs(v, -1, tree) * 2

	@cache
	def get_max_distance(u, v):
		leaves.add(u)
		leaves.add(v)
		return max_distance + get_distance(u, v)

	@cache
	def get_max_distance_for_leaves(u):
		return max_distance + get_distance(u, next(iter(leaves - {u})))

	queue = deque([(i, get_max_distance_for_leaves(i)) for i in range(1, 1 + n) if len(tree[i]) == 1])
	max_distance = 0
	result = []
	while queue:
		node, distance = queue.popleft()
		max_distance = max(max_distance, distance)
		result.append((node, next(iter(leaves)), next(iter(leaves)), node))
		leaves.remove(node)
		for child in tree[node]:
			if child != -1 and len(tree[child]) == 1:
				queue.append((child, get_max_distance_for_leaves(child)))
			elif child != -1:
				tree[child].remove(node)
				tree[node].remove(child)

	print(max_distance)
	for node, u, v, c in result[::-1]:
		print(u, v, c)


solve()
