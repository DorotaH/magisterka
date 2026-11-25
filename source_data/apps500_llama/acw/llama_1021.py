import sys


class SegmentTree:
	def __init__(self, nums):
		self.n = len(nums)
		self.tree = [0] * (self.n * 4)
		self.build(0, 0, self.n - 1, nums)

	def build(self, node, start, end, nums):
		if start == end:
			self.tree[node] = nums[start]
		else:
			mid = (start + end) // 2
			self.build(2 * node + 1, start, mid, nums)
			self.build(2 * node + 2, mid + 1, end, nums)
			self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

	def query(self, node, start, end, l, r):
		if l > end or start > r:
			return -float('inf')
		if start >= l and r >= end:
			return self.tree[node]
		mid = (start + end) // 2
		return max(self.query(2 * node + 1, start, mid, l, r),
				self.query(2 * node + 2, mid + 1, end, l, r))

	def get(self, l, r):
		return self.query(0, 0, self.n - 1, l, r)


def main():
	input = sys.stdin.readline
	print = sys.stdout.write
	n, m = map(int, input().split())
	intervals = []
	for _ in range(n):
		l, r = map(int, input().split())
		intervals.append((l, r))

	intervals.sort(key=lambda x: x[1])
	segments = []
	for i in range(n):
		if not segments or intervals[i][0] > segments[-1][1]:
			segments.append(intervals[i])
		else:
			segments[-1] = (segments[-1][0], max(segments[-1][1], intervals[i][1]))

	segment_tree = SegmentTree(segments)
	for _ in range(m):
		x, y = map(int, input().split())
		ans = float('inf')
		l, r = x, y
		while l <= r:
			ans = min(ans, segment_tree.get(l, r) - x + 1)
			l = segments[segment_tree.get(l, r) - x][0]
			r = segments[segment_tree.get(l, r) - x][1]
		if ans == float('inf'):
			print('-1 ')
		else:
			print(' ' + str(ans))
		print('')


if __name__ == '__main__':
	main()
