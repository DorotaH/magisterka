import sys
import bisect


def read_ints():
	return map(int, sys.stdin.readline().split())


def read_int():
	return int(sys.stdin.readline())


def read_string():
	return sys.stdin.readline().strip()


def read_strings():
	return map(lambda s: s.strip(), sys.stdin.readline().split())


def print_list(l):
	print(' '.join(map(str, l)))


def print_line(s):
	print(s)


def print_yes_no(b):
	print('YES' if b else 'NO')


def debug(*args):
	if DEBUG:
		print(*args)


def ceil(a, b):
	return -(-a // b)


class BIT:
	def __init__(self, n):
		self.n = n
		self.tree = [0] * (1 + n)

	def update(self, i, x):
		while i <= self.n:
			self.tree[i] += x
			i += i & -i

	def query(self, i):
		res = 0
		while i:
			res += self.tree[i]
			i -= i & -i
		return res

	def range_query(self, l, r):
		return self.query(r) - self.query(l - 1)


class SegmentTree:
	def __init__(self, a):
		self.n = len(a)
		self.tree = [0] * (self.n * 4)
		self.build(a, 0, 0, self.n - 1)

	def build(self, a, v, tl, tr):
		if tl == tr:
			self.tree[v] = a[tl]
		else:
			tm = (tl + tr) // 2
			self.build(a, 2 * v + 1, tl, tm)
			self.build(a, 2 * v + 2, tm + 1, tr)
			self.tree[v] = max(self.tree[2 * v + 1], self.tree[2 * v + 2])

	def update(self, v, tl, tr, pos, new_val):
		if tl == tr:
			self.tree[v] = new_val
		else:
			tm = (tl + tr) // 2
			if pos <= tm:
				self.update(2 * v + 1, tl, tm, pos, new_val)
			else:
				self.update(2 * v + 2, tm + 1, tr, pos, new_val)
			self.tree[v] = max(self.tree[2 * v + 1], self.tree[2 * v + 2])

	def query(self, v, tl, tr, l, r):
		if tl >= l and tr <= r:
			return self.tree[v]
		elif tl > r or l > tr:
			return float('-inf')
		else:
			tm = (tl + tr) // 2
			return max(self.query(2 * v + 1, tl, tm, l, r),
					self.query(2 * v + 2, tm + 1, tr, l, r))

	def query(self, l, r):
		return self.query(0, 0, self.n - 1, l, r)


DEBUG = False

n, m = read_ints()
intervals = []
for _ in range(n):
	l, r = read_ints()
	intervals.append((l, r))

intervals.sort(key=lambda x: x[1])

BIT = BIT(5 * 10**5 + 1)
for l, r in intervals:
	BIT.update(l, 1)
	BIT.update(1 + r, -1)

res = []
for _ in range(m):
	x, y = read_ints()
	queries = [x, y]
	queries.sort()
	index = bisect.bisect_left([i[0] for i in intervals], queries[0])
	if index == len(intervals) or queries[1] > intervals[index][1]:
		res.append(-1)
		continue
	if index == 0:
		res.append(1)
		continue
	if intervals[index][0] <= queries[0] and intervals[index - 1][1] >= queries[1]:
		res.append(2)
		continue
	if intervals[index][0] < queries[0] and intervals[index - 1][1] > queries[1]:
		res.append(2)
		continue

	if BIT.range_query(queries[0], queries[1]):
		res.append(1)
	else:
		res.append(-1)

print_line(' '.join(map(str, res)))
