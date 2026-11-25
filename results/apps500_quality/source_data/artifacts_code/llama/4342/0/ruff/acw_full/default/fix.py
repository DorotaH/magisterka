from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
G = [[] for _ in range(n)]
for _ in range(n - 1):
	u, v = map(int, stdin.readline().split())
	G[u - 1].append(v - 1)
	G[v - 1].append(u - 1)

visited = [False] * n
stack = [0]
while stack:
	u = stack.pop()
	visited[u] = True
	for v in G[u]:
		if not visited[v]:
			stack.append(v)

color_u = a[:]
color_v = a[:]
for u in range(n):
	for v in G[u]:
		if a[u] == 2:
			color_v[v] = 2
		elif a[v] == 2:
			color_u[v] = 2

ans = 0
for u in range(n):
	for v in G[u]:
		if (color_u[u] == 1 or color_v[v] == 1) and (color_u[v] == 1 or color_v[u] == 1):
			continue
		ans += 1

print(ans)
