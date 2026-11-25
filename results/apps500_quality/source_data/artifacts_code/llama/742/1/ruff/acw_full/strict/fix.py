

def solve():
	n = int(input())
	b = list(map(int, input().split()))

	used = [False] * (2 * n + 1)

	for i in range(n):
		used[b[i]] = True

	a = [i for i in range(1, 2 * n + 1) if not used[i]]
	for i in range(n):
		used[b[i]] = True
		a.append(b[i])
		for j in range(1, 2 * n + 1):
			if used[j]:
				a.append(j)
				used[j] = False

	if len(a) != 2 * n:
		print(-1)
	else:
		print(*a)


t = int(input())
for _ in range(t):
	solve()
	print()
