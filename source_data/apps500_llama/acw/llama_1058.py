import sys


def solve():
	n = int(sys.stdin.readline().strip())
	w = list(map(int, sys.stdin.readline().strip().split()))
	order = sys.stdin.readline().strip()
	empty = []
	occupied = []
	for i in range(n):
		if order[i] == '0':
			empty.append(i + 1)
		else:
			occupied.append(i + 1)

	ans = []
	used = [0] * n
	for i in range(len(empty)):
		ans.append(1 + empty[i])
		used[empty[i]] = 1
	for _ in range(len(occupied)):
		max_i = -1
		max_w = 0
		for j in range(n):
			if used[j] == 1 and max_w < w[j]:
				max_i = j
				max_w = w[j]
		ans.append(max_i + 1)
		used[max_i] = 2
	print(' '.join(map(str, ans)))


solve()
