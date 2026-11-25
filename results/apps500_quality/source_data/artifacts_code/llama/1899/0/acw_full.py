import sys
from bisect import bisect_right

input = sys.stdin.readline

n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
a = [-a[i] for i in range(n)]
b = [[] for _ in range(1 + n)]
for _ in range(s):
	l, r = map(int, input().split())
	b[l - 1].append(r)

f = [0] * (1 + n)
for i in range(n):
	for x in b[i]:
		f[x] += 1

g = [0] * (1 + n)
for i in range(1, 1 + n):
	g[i] = g[i - 1] + f[i]

ans = -1
for l in range(1, 1 + n):
	if g[r - 1] - g[l - 1] >= k:
		c = [0] * (1 + n)
		for i in range(l, r):
			c[i] = 1
		for i in range(l, r):
			for x in b[i]:
				c[x] += 1
		for i in range(l, r):
			for x in b[i]:
				c[x] = 0

		p = [0] * (1 + n)
		for i in range(1, 1 + n):
			p[i] = p[i - 1] + c[i]
		v = [0] * (1 + n)
		for i in range(1, 1 + n):
			v[p[i]] = a[i - 1]

		ans = a[l - 1] if k <= p[r - 1] else -1

		break

print(-1 if ans == -1 else -ans)
