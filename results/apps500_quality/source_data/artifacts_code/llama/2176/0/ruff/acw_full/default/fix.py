
MOD = 998244353


class FenwickTree:
	def __init__(self, n):
		self.n = n
		self.t = [0] * (1 + n)

	def update(self, x, delta):
		while self.n > x:
			self.t[x] += delta
			x |= 1 + x

	def pref_sum(self, r):
		s = 0
		while 0 <= r:
			s += self.t[r]
			r = (r & (1 + r)) - 1
		return s


def solve():
	n = int(input())
	fenwick1 = FenwickTree(n)
	fenwick2 = FenwickTree(n)
	a, b = [], []
	for _ in range(n):
		a_i, b_i = map(int, input().split())
		a.append(a_i)
		b.append(b_i)

	for i in range(n):
		fenwick1.update(a[i], 1)
		fenwick2.update(b[i], 1)

	ans = next(
		(
			0
			for i in range(n)
			if 1 < fenwick1.pref_sum(a[i] - 1)
			or 1 < fenwick2.pref_sum(b[i] - 1)
		),
		1,
	)
	for i in range(n):
		cnt = [0] * (1 + n)
		cnt[a[i]] += 1
		cnt[b[i]] += 1
		if 1 < cnt[a[i]] or cnt[b[i]] > 1:
			ans = ans * (n - i) % MOD

	print(ans)


solve()
