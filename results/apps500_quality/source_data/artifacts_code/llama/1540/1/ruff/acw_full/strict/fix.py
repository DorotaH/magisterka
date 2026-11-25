
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
log = [tuple(map(int, input().split())) for _ in range(k)]
d = [0] * n
for x, y in log:
	x -= 1
	y -= 1
	for i in range(n):
		if a[i][y]:
			d[i] += 1

print(*d)
