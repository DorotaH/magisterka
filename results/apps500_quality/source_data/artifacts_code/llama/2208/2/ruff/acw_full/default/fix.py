import sys


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class SegmentTree:
	def __init__(self, n):
		self.n = n
		self.tree = [None] * (4 * n)
		self.build(0, 0, self.n - 1)

	def build(self, node, start, end):
		if start == end:
			self.tree[node] = Node(sys.maxsize)
		else:
			mid = (start + end) // 2
			self.build(2 * node + 1, start, mid)
			self.build(2 * node + 2, mid + 1, end)
			self.tree[node] = Node(min(self.tree[2 * node + 1].value, self.tree[2 * node + 2].value))

	def update(self, index, value):
		self.update(0, 0, self.n - 1, index, value)

	def update(self, node, start, end, index, value):
		if start == end:
			self.tree[node].value = min(self.tree[node].value, value)
		else:
			mid = (start + end) // 2
			if mid >= index:
				self.update(2 * node + 1, start, mid, index, value)
			else:
				self.update(2 * node + 2, mid + 1, end, index, value)
			self.tree[node].value = min(self.tree[2 * node + 1].value, self.tree[2 * node + 2].value)

	def query(self, l, r):
		return self.query(0, 0, self.n - 1, l, r)

	def query(self, node, start, end, l, r):
		if l > end or start > r:
			return sys.maxsize
		if start >= l and r >= end:
			return self.tree[node].value
		mid = (start + end) // 2
		return min(self.query(2 * node + 1, start, mid, l, r), self.query(2 * node + 2, mid + 1, end, l, r))


def read_input():
	n = int(sys.stdin.readline())
	a = list(map(int, sys.stdin.readline().split()))
	b = list(map(int, sys.stdin.readline().split()))
	return n, a, b


def main():
	n, a, b = read_input()
	a_tree = SegmentTree(n)
	for i in range(n):
		a_tree.update(i, a[i])
	b_tree = SegmentTree(n)
	for i in range(n):
		b_tree.update(i, b[i])
	ans = 0
	for l in range(n):
		for r in range(l, n):
			if a_tree.query(l, r) == b_tree.query(l, r):
				ans += 1
	print(ans)


if __name__ == "__main__":
	main()
