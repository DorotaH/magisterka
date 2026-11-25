import sys


def solve():
	n = int(sys.stdin.readline())
	b = list(map(int, sys.stdin.readline().split()))

	a = [0] * (2 * n)
	used = [False] * (2 * n + 1)

	for i in range(n):
		a[i * 2] = b[i]
		used[b[i]] = True

	j = 1
	for i in range(1, 2 * n + 1):
		if not used[i]:
			a[i * 2 - 1] = i
			while not used[j]:
				j += 1
			a[i * 2] = j
			used[j] = True

	for i in range(2 * n):
		if a[i] > a[i + 1]:
			print(-1)
			return

	print(' '.join(map(str, a)))


t = int(sys.stdin.readline())
for _ in range(t):
	solve()
