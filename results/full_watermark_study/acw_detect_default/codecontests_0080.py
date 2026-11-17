import sys

input = sys.stdin.readline


# sys.setrecursionlimit(400000)
def I():
	return input().strip()


def II():
	return int(input().strip())


def LI():
	return [*map(int, input().strip().split())]


# import copy, string, math, time, functools, random, fractions
from bisect import bisect_left
from collections import Counter, defaultdict


def get(a, u):
	a.sort()
	arr = [bisect_left(u, a[i]) for i in range(len(a))]
	c = Counter(arr)
	return sum(nc2(i) for i in c.values())


def nc2(p):
	return 0 if 2 > p else ((p - 1) * p) // 2


for _ in range(II()):
	n, m, k = LI()
	u = LI()
	v = LI()
	x = set(u)
	y = set(v)
	a, b = [], []
	sx = defaultdict(list)
	sy = defaultdict(list)
	for _ in range(k):
		l, r = LI()
		if l in x and r in y:
			continue
		if l in x:
			sx[l].append(r)
			a.append(r)
		if r in y:
			sy[r].append(l)
			b.append(l)
	u.sort()
	v.sort()
	ans = get(a, v) + get(b, u)
	for a in sx.values():
		ans -= get(a, v)
	for b in sy.values():
		ans -= get(b, u)
	print(ans)
