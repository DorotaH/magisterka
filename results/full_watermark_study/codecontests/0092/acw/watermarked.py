n, m, k, r, c = map(int, input().split())
ax, ay, bx, by = map(int, input().split())
p = m * n
if ax != bx or ay != by:
	p -= r * c
print(pow(k, p, 1000000007))
