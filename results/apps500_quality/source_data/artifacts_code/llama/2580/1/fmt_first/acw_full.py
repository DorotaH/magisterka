import sys

input = sys.stdin.readline


class Tree:
	def __init__(self, n, edges, primes, powers):
		self.n = n
		self.edges = edges
		self.primes = primes
		self.powers = powers
		self.factorization = {}
		self.parent = [-1] * (1 + n)
		self.depth = [0] * (1 + n)
		self.n1 = 0
		self.n2 = 0
		self.res = 0

	def dfs(self, u, p):
		self.parent[u] = p
		for v in self.edges[u]:
			if v != p:
				self.depth[v] = self.depth[u] + 1
				self.dfs(v, u)
		self.dfs1(u)

	def dfs1(self, u, p=None):
		if p is not None:
			self.n1 += self.powers[self.primes.index(self.primes[u])][0]
			self.n2 += self.powers[self.primes.index(self.primes[u])][1]
		for v in self.edges[u]:
			if v != p:
				self.dfs1(v, u)

	def power(self, x, y):
		res = 1
		while y:
			if y % 2 == 1:
				res *= x
				res %= 1000000007
			x *= x
			x %= 1000000007
			y //= 2
		return res

	def solve(self):
		self.dfs(1)
		for _ in range(self.n2):
			self.n2 -= 1
			self.n1 += 1
		self.n1 %= 1000000007
		for _ in range(self.n2):
			self.n2 -= 1
			self.n1 -= 1
		self.n1 %= 1000000007
		self.n2 %= 1000000007
		self.res = self.n2 * self.power(2, self.n1)
		self.res %= 1000000007
		for p in self.primes:
			if p != 2:
				self.res = self.res * self.power(
					p, self.powers[self.primes.index(p)][1]
				)
				self.res %= 1000000007
		for i in range(1, self.n):
			for j in range(i + 1, self.n):
				self.res = (
					self.res
					+ (self.depth[i] + self.depth[j])
					* (self.n - self.depth[i] - self.depth[j])
				) % 1000000007
		print(self.res)


t = int(input())
for _ in range(t):
	n = int(input())
	edges = [[] for _ in range(1 + n)]
	for _ in range(n - 1):
		u, v = map(int, input().split())
		edges[u].append(v)
		edges[v].append(u)
	m = int(input())
	primes = list(map(int, input().split()))
	powers = []
	for p in primes:
		power1 = 0
		power2 = 0
		while p % 2 == 0:
			p //= 2
			power2 += 1
		power1 = n - power2
		powers.append([power1, power2])
	tree = Tree(n, edges, primes, powers)
	tree.solve()
