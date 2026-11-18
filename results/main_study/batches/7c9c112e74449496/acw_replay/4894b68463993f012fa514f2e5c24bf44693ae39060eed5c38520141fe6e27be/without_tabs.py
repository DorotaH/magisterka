import sys
from collections import Counter
from heapq import heappop, heappush
from operator import itemgetter

n, m, k = list(map(int, input().split()))
points = [list(map(int, line.split())) for line in sys.stdin]
pts_sorted_x = sorted(points)
pts_sorted_y = sorted(points, key=itemgetter(1, 0))
inf = 1 + 10**9
OK = (inf, inf)


def solve2(imos, t):
	acc, cur = 0, 0

	for k in sorted(imos.keys()):
		if t < k:
			break
		if 0 >= acc and cur + 1 < k or imos[k] + acc <= 0:
			acc = 0
			break
		acc += imos[k]

	return 0 >= acc


def add_imos(imos, x, y):
	imos[x] += y
	if imos[x] == 0:
		del imos[x]


def solve(t, px=-1, py=-1):
	set_x = {1, n}
	set_y = {1, m}

	for x, y in points:
		set_x.update((max(1, x - t), max(1, x - t - 1), min(n, t + x), min(n, t + x + 1)))
		set_y.update((max(1, y - t), max(1, y - t - 1), min(m, t + y), min(m, t + y + 1)))

	ans_x = ans_y = inf
	pi, imos, hq = 0, Counter(), []
	if px != -1:
		imos[py] += 1
		imos[py + t * 2 + 1] -= 1

	for cx in sorted(set_x):
		while hq and hq[0][0] < cx:
			add_imos(imos, hq[0][1], -1)
			add_imos(imos, hq[0][2], +1)
			heappop(hq)
		while pi < k and pts_sorted_x[pi][0] - t <= cx <= t + pts_sorted_x[pi][0]:
			x, y = pts_sorted_x[pi]
			add_imos(imos, max(1, y - t), 1)
			add_imos(imos, t + y + 1, -1)
			heappush(hq, (t + x, max(1, y - t), t + y + 1))
			pi += 1

		if solve2(imos, m):
			ans_x = cx
			break

	pi = 0
	imos.clear()
	hq.clear()
	if px != -1:
		imos[px] += 1
		imos[px + t * 2 + 1] -= 1

	for cy in sorted(set_y):
		while hq and hq[0][0] < cy:
			add_imos(imos, hq[0][1], -1)
			add_imos(imos, hq[0][2], +1)
			heappop(hq)
		while pi < k and pts_sorted_y[pi][1] - t <= cy <= t + pts_sorted_y[pi][1]:
			x, y = pts_sorted_y[pi]
			add_imos(imos, max(1, x - t), 1)
			add_imos(imos, t + x + 1, -1)
			heappush(hq, (t + y, max(1, x - t), t + x + 1))
			pi += 1

		if solve2(imos, n):
			ans_y = cy
			break

	return ans_x, ans_y


ok, ng = 1 + 10**9, -1
while 1 < abs(ok - ng):
	mid = (ng + ok) >> 1
	p = solve(mid)
	if p == OK:
		ok = mid
		continue

	if solve(mid, p[0], p[1]) == OK:
		ok = mid
	else:
		ng = mid

print(ok)
