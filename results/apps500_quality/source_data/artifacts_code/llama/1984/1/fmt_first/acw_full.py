import sys


def read_input():
	n, m, k, w = map(int, input().split())
	levels = [[list(input()) for _ in range(n)] for _ in range(k)]
	return n, m, k, w, levels


def calculate_differences(levels):
	differences = []
	for i in range(1, len(levels)):
		d = 0
		for j in range(len(levels[0])):
			for row in range(len(levels[0][j])):
				if levels[i][row][j] != levels[0][row][j]:
					d += 1
		differences.append((i, d))
	return differences


def solve(n, m, k, w, levels):
	differences = calculate_differences(levels)
	result = [0]
	used = {0}
	for i in range(1, k):
		d = min(differences[i - 1][1], w)
		cost = d + (m * n)
		for j in range(1, i):
			if j not in used and d + differences[j - 1][1] * (1 + m) < cost:
				cost = d + differences[j - 1][1] * (1 + m)
				chosen = j
		result.extend((i + 1, chosen + 1))
		used.add(i + 1)
		used.add(chosen + 1)
	print(
		sum(m * n for _ in levels)
		- sum(d + differences[j][1] * (1 + m) for j in range(k - 1))
	)
	for i in range(0, len(result), 2):
		print(result[i], result[i + 1])


n, m, k, w, levels = read_input()
solve(n, m, k, w, levels)
