from collections import defaultdict
import sys


def find(x, parent):
	if parent[x] != x:
		parent[x] = find(parent[x], parent)
	return parent[x]


def union(x, y, parent, rank):
	root_x, root_y = find(x, parent), find(y, parent)
	if root_x != root_y:
		if rank[root_y] < rank[root_x]:
			parent[root_y] = root_x
		else:
			parent[root_x] = root_y
			if rank[root_x] == rank[root_y]:
				rank[root_y] += 1
	return


n = int(input())
parent = {i: i for i in range(n)}
rank = n * [1]
words = [input().strip() for _ in range(n)]
chars = defaultdict(list)
for i, word in enumerate(words):
	for char in word:
		chars[char].append(i)

ans = n
for char in chars:
	for i in chars[char]:
		for j in chars[char]:
			if i != j:
				union(i, j, parent, rank)
	root = find(0, parent)
	if parent[root] != root:
		ans = min(ans, len([x for x in parent if find(x, parent) == root]))

print(ans)
