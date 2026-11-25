import sys

n, m, a, b = map(int, input().split())
g0, x, y, z = map(int, input().split())

g = [0] * (m * n)
g[0] = g0

for i in range(1, m * n):
	g[i] = (g[i - 1] * x + y) % z

heights = [0] * (1 + m)
for j in range(m):
	min_height = g[j]
	for i in range(j, m * n, m):
		min_height = min(min_height, g[i])
	heights[1 + j] = min_height

prefix_heights = [0] * (1 + m)
for i in range(m):
	prefix_heights[i + 1] = prefix_heights[i] + heights[i + 1]

ans = 0
for i in range(a):
	min_height = float("inf")
	for j in range(b):
		min_height = min(min_height, heights[j + i * m])
	ans += min_height

	for k in range(i + 1, a):
		min_height = float("inf")
		for j in range(b):
			min_height = min(min_height, heights[j + k * m])
		ans += min_height

	for k in range(i, a):
		ans -= prefix_heights[(k + 1) * m] - prefix_heights[i * m]

print(ans)
