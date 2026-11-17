import sys
input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	u -= 1
	v -= 1

	if 48 <= u or 48 <= v:
		continue

	G[u].append(v)
	G[v].append(u)

if 48 <= n:
	G = G[:48]


def ok(a, b, c, d, e):
	allfd = True
	nofd = True

	people = [a, b, c, d, e]
	for x in people:
		for y in people:
			if x == y:
				continue
			if x in G[y]:
				nofd = False
			else:
				allfd = False

	return allfd or nofd


sz = len(G)
for a in range(sz):
	for b in range(a + 1, sz):
		for c in range(1 + b, sz):
			for d in range(1 + c, sz):
				for e in range(1 + d, sz):
					if ok(a, b, c, d, e):
						ans = [a, b, c, d, e]
						print(*[1 + x for x in ans])
						exit()

print(-1)
