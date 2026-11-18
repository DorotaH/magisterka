#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect


def LI():
	return [int(x) for x in sys.stdin.readline().split()]


def I():
	return int(sys.stdin.readline())


def LS():
	return [list(x) for x in sys.stdin.readline().split()]


def S():
	res = list(sys.stdin.readline())
	return res[:-1] if res[-1] == "\n" else res


def IR(n):
	return [I() for _ in range(n)]


def LIR(n):
	return [LI() for _ in range(n)]


def SR(n):
	return [S() for _ in range(n)]


def LSR(n):
	return [LS() for _ in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def solve():
	n, k = LI()
	a = LI()
	a.sort()
	d = defaultdict(lambda: 0)
	c = defaultdict(lambda: 0)
	s = [0]
	for i in a:
		d[i] += i
		c[i] += 1
		s.append(i + s[-1])
	ans = float("inf")
	p = -1
	for i in a:
		if i == p:
			continue
		if c[i] >= k:
			ans = 0
			break
		l, r = bisect.bisect_left(a, i), bisect.bisect_right(a, i)
		m = r
		if k <= m:
			ns = l * (i - 1) - s[l]
			su = k + ns - c[i]
			ans = min(ans, su)
		m = n - l
		if k <= m:
			ns = s[n] - s[r] - (n - r) * (i + 1)
			su = k + ns - c[i]
			ans = min(ans, su)
		ns = s[n] - s[r] - (n - r) * (i + 1) + l * (i - 1) - s[l]
		su = k + ns - c[i]
		ans = min(ans, su)
		p = i
	print(ans)
	return


# Solve


def __starting_point():
	solve()


__starting_point()
