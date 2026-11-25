import sys


class FenwickTree:
	def __init__(self, n):
		self.n = n
		self.t = [0] * (1 + n)

	def update(self, i, delta):
		while i <= self.n:
			self.t[i] += delta
			i += i & -i

	def query(self, i):
		res = 0
		while i:
			res += self.t[i]
			i -= i & -i
		return res

	def range_query(self, l, r):
		return self.query(r) - self.query(l - 1)


def solve():
	n = int(sys.stdin.readline())
	a = list(map(int, sys.stdin.readline().split()))
	b = list(map(int, sys.stdin.readline().split()))

	max_values = FenwickTree(n)
	for i in range(n):
		max_values.update(i + 1, a[i])

	min_values = FenwickTree(n)
	for i in range(n):
		min_values.update(i + 1, b[i])

	ans = 0
	max_right = [0] * (1 + n)
	for i in range(n - 1, -1, -1):
		max_right[i] = max(a[i], max_right[i + 1])

	for i in range(n):
		l = 1
		while i > l:
			l *= 2
		for r in range(l, 1 + n, l):
			if l + r <= n:
				max_val = max_right[l + r]
				min_val = min_values.range_query(l, l + r)
				if max_val == min_val:
					ans += 1
		l = 2 * l if l else 1

	print(ans)


solve()
