import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n, k, x = mints()
a = list(mints())
d = [None] * (1 + n)
p = [None] * (1 + n)
for i in range(0, k):
	d[i] = a[i]
for _ in range(2, 1 + x):
	d, p = p, d
	for nn in range(n):
		m = None
		for i in range(max(0, nn - k), nn):
			if p[i] != None:
				m = p[i] if m == None else max(m, p[i])
		d[nn] = m + a[nn] if m != None else None
m = -1
for i in range(n - k, n):
	if d[i] != None:
		m = max(m, d[i])
print(m)