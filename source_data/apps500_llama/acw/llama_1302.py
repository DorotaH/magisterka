import sys

n = int(input())
q = [list(map(int, input().split())) for _ in range(n - 2)]

a = [0] * n
for i in range(n - 2):
	a[i] = q[i][0]
	a[i + 1] = q[i][1]
	a[i + 2] = q[i][2]

visited = [False] * (1 + n)
for i in range(n - 2):
	if a[i] != a[i + 1] and a[i] != a[i + 2] and a[i + 1] != a[i + 2]:
		print("NO")
		sys.exit()

for i in range(n):
	if not visited[a[i]]:
		visited[a[i]] = True
	for j in range(i + 1, n):
		if not visited[a[j]]:
			a[j], a[i + 1] = a[i + 1], a[j]
			visited[a[j]] = True
			break
print(*a)
