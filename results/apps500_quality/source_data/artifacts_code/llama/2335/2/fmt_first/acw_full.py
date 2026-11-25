import sys
import math
from collections import deque

input = sys.stdin.readline


class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank = [0] * n
		self.color = [0] * n

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		root_x = self.find(x)
		root_y = self.find(y)
		if root_x != root_y:
			if self.rank[root_x] > self.rank[root_y]:
				self.parent[root_y] = root_x
			elif self.rank[root_x] < self.rank[root_y]:
				self.parent[root_x] = root_y
			else:
				self.parent[root_y] = root_x
				self.rank[root_x] += 1
			self.color[root_x] |= self.color[root_y]
			self.color[root_y] = 0


def main():
	n = int(input())
	points = []
	for _ in range(n):
		p, c = input().split()
		points.append((int(p), c))

	uf = UnionFind(n)
	for i in range(n):
		uf.color[i] = 1 if points[i][1] == "R" else 2 if points[i][1] == "B" else 0

	total_cost = 0
	queue = deque()
	for i in range(n):
		if uf.find(i) == i:
			queue.append(i)

	while queue:
		node = queue.popleft()
		for i in range(n):
			if 1000000000 > points[node][0] - points[i][0] and uf.find(i) != uf.find(
				node
			):
				uf.union(i, node)
				total_cost += abs(points[node][0] - points[i][0])
				queue.append(i)

	total_cost *= 2
	red_connected = False
	for i in range(n):
		if uf.color[uf.find(i)] == 3:
			if red_connected:
				total_cost -= abs(points[i][0] - points[j][0])
			else:
				red_connected = True
				j = i
	print(total_cost)


if __name__ == "__main__":
	main()
