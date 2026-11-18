import numpy as np

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def naiseki(a, b):
	return a[0] * b[0] + b[1] * a[1] > 0.0


ans = 0

for i in range(1001):
	xl = np.cos(2.0 * np.pi * i / 1000.0)
	yl = np.sin(2.0 * np.pi * i / 1000.0)
	x = 0
	y = 0
	for j in range(n):
		if naiseki([xl, yl], xy[j]):
			x += xy[j][0]
			y += xy[j][1]
	ans = max(ans, np.sqrt(x**2 + y**2))
print(ans)
