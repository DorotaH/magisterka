from collections import deque
import sys


def solve():
	n, m = map(int, input().split())
	w = list(map(int, input().split()))
	x, y = [], []
	for _ in range(m):
		xi, yi = map(int, input().split())
		x.append(xi - 1)
		y.append(yi - 1)

	z = []
	for i in range(m):
		if w[x[i]] == 0 and w[y[i]] == 0:
			z.append(i)
		elif w[x[i]] == 0:
			z.append(i)
		elif w[y[i]] == 0:
			z.append(i)
		else:
			z.append(-1)

	z.sort(key=lambda x: -w[x] if w[x] != 0 else -10**9)
	z = deque(z)
	visited = set(z)

	ans = []
	for _ in range(m):
		if z[0] == -1:
			print("DEAD")
			return
		if w[x[z[0]]] == 0:
			w[y[z[0]]] -= 1
			if w[y[z[0]]] == 0:
				visited.add(y[z[0]])
				w[y[z[0]]] = 0
		else:
			w[x[z[0]]] -= 1
			if w[x[z[0]]] == 0:
				visited.add(x[z[0]])
				w[x[z[0]]] = 0
		ans.append(z[0] + 1)
		if z[0] in visited:
			z.popleft()
		else:
			while z and z[0] not in visited:
				z.popleft()
			if not z:
				print("DEAD")
				return
			z.rotate(-1)

	if z:
		print("DEAD")
	else:
		print("ALIVE")
		print(*ans)


if __name__ == "__main__":
	solve()
