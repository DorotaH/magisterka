N, M = map(int, input().split())
Edge = []
for _ in range(M):
	a, b = map(int, input().split())
	a, b = a - 1, b - 1
	Edge.append([a, b])


class UnionFind:
	def __init__(self, n):
		self.par = list(range(n))
		self.rank = [0] * n
		self.size = n * [1]

	# 検索
	def find(self, x):
		if self.par[x] == x:
			return x
		self.par[x] = self.find(self.par[x])
		return self.par[x]

	# 併合
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return

		if self.rank[y] > self.rank[x]:
			self.par[x] = y
			self.size[y] += self.size[x]
			self.size[x] = 0
		else:
			self.par[y] = x
			self.size[x] += self.size[y]
			self.size[y] = 0
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1

	# 同じ集合に属するか判定
	def same(self, x, y):
		return self.find(x) == self.find(y)

	# すべての頂点に対して親を検索する
	def all_find(self):
		for n in range(len(self.par)):
			self.find(n)


UF = UnionFind(N)
Score = (N - 1) * N // 2
ans = []
while Edge:
	ans.append(Score)
	a, b = Edge.pop()
	pa, pb = UF.find(a), UF.find(b)
	if not UF.same(pa, pb):
		Score -= UF.size[pb] * UF.size[pa]
	UF.union(a, b)

print(*ans[::-1], sep="\n")
