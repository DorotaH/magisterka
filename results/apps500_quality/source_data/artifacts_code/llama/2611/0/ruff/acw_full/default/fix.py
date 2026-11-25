import sys


class SegmentTree:
	def __init__(self, n, data=None):
		self.n = n
		self.size = n
		self.data = [0] * (2 * self.size)
		if data is not None:
			for i in range(self.n):
				self.data[i + self.size] = data[i]
			for i in range(self.size - 1, 0, -1):
				self.data[i] = self.query(i * 2 + 1, i * 2 + 2)

	def _set(self, i, v):
		i += self.size
		self.data[i] = v
		i //= 2
		while i > 0:
			self.data[i] = max(self.data[i * 2], self.data[i * 2 + 1])
			i //= 2

	def set(self, i, v):
		if i < 0 or i >= self.n:
			raise ValueError("set() indices must be in the range [0, n)")
		self._set(i, v)

	def _query(self, l, r):
		l += self.size
		r += self.size
		ans = 0
		while l < r:
			if l & 1:
				ans = max(ans, self.data[l])
				l += 1
			if r & 1:
				r -= 1
				ans = max(ans, self.data[r])
			l //= 2
			r //= 2
		return ans

	def query(self, l, r):
		return 0 if l >= self.n or 0 >= r or l > r else self._query(l, r)

	def __str__(self):
		return "[" + ", ".join(map(str, self.data[self.size:self.size + self.n])) + "]"


def main():
	input = sys.stdin.readline
	n, q = map(int, input().split())
	p = list(map(int, input().split()))
	xs = sorted(set(p))
	x_to_i = {x: i for i, x in enumerate(xs)}

	st = SegmentTree(len(xs))
	for x in p:
		st.set(x_to_i[x], 1)

	m = len(xs)
	moves = 0
	for _ in range(q):
		t, x = map(int, input().split())
		if t == 0:
			st.set(x_to_i[x], -1)
		else:
			st.set(x_to_i[x], 1)
		if st.query(0, m) > 1:
			moves = 2 * (m - 1 - st.query(0, m)) + 2 * (st.query(0, m) - 1)
		else:
			moves = 0
		print(moves)


if __name__ == '__main__':
	main()
