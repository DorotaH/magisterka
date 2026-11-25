import sys

N = 100000
M = 200000
D = 10000


class DSU:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank = [0] * n

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x != y:
			if self.rank[y] < self.rank[x]:
				x, y = y, x
			self.parent[x] = y
			if self.rank[x] == self.rank[y]:
				self.rank[y] += 1
			if self.rank[y] > self.rank[x]:
				self.parent[x] = y


def read_input():
	n, m = map(int, sys.stdin.readline().split())
	dsu = DSU(2 + n)
	pairs = []
	for _ in range(m):
		l, r, d = map(int, sys.stdin.readline().split())
		if d > 0:
			pairs.append((l - 1, r - 1, d))
		else:
			dsu.union(l - 1, r - 1)
	return n, dsu, pairs


def solve(n, dsu, pairs):
	for l, r, d in pairs:
		if dsu.find(l) != dsu.find(r) and d != abs(r - l):
			return False
	return True


def main():
	n, dsu, pairs = read_input()
	if solve(n, dsu, pairs):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
