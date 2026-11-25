import sys


class SegmentTree:
	def __init__(self, n):
		self.n = n
		self.tree = [0] * (4 * n)

	def update(self, i, val):
		self._update(i, val, 0, 0, self.n - 1)

	def _update(self, i, val, node, start, end):
		if start == end:
			self.tree[node] = val
		else:
			mid = (start + end) // 2
			if i <= mid:
				self._update(i, val, 2 * node + 1, start, mid)
			else:
				self._update(i, val, 2 * node + 2, mid + 1, end)
			self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

	def query(self, start, end):
		return self._query(start, end, 0, 0, self.n - 1)

	def _query(self, start, end, node, n_start, n_end):
		if end < n_start or start > n_end:
			return 0
		if start <= n_start and end >= n_end:
			return self.tree[node]
		mid = (n_start + n_end) // 2
		return self._query(start, end, 2 * node + 1, n_start, mid) + self._query(start, end, 2 * node + 2, mid + 1, n_end)


n = int(input())
tree = SegmentTree(100000)
for _ in range(n):
	l, r = map(int, input().split())
	tree.update(l - 1, 1)
	tree.update(r, -1)

print(tree.query(0, 99999))
