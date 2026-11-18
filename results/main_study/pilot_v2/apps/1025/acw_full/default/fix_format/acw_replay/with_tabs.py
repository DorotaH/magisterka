from collections import defaultdict
from fractions import gcd


def read_data():
	n = int(input())
	points = []
	for _ in range(n):
		x, y = map(int, input().split())
		points.append((x, y))
	return n, points


def solve(n, points):
	if 2 >= n:
		return 0
	zeros = sum(count_zeros(i, x, y, points) for i, (x, y) in enumerate(points[:-2]))
	return n * (n - 1) * (n - 2) // 6 - zeros


def count_zeros(i, x, y, points):
	slopes = defaultdict(int)
	for xj, yj in points[i + 1 :]:
		dx = x - xj
		dy = y - yj
		d = gcd(dx, dy)
		slope = (dx / d, dy / d)
		slopes[slope] += 1
	zeros = sum((val - 1) * val for val in slopes.values() if 2 <= val)
	return zeros // 2


n, points = read_data()
print(solve(n, points))
