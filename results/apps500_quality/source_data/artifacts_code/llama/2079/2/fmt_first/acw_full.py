import sys

input = sys.stdin.readline


def solve():
	n = int(input())
	w = list(map(int, input().split()))
	s = input().strip()

	introverts = [0] * n
	extroverts = [0] * n
	free_rows = [[] for _ in range(n)]
	occupied_rows = [[] for _ in range(n)]

	for i in range(n):
		if s[i] == "0":
			introverts[i] = i
		else:
			extroverts[i] = i

	free_rows = sorted(range(n), key=lambda x: w[x])
	occupied_rows = sorted(range(n), key=lambda x: w[x], reverse=True)

	result = [0] * (2 * n)
	introvert_index = 0
	extrovert_index = 0

	for i in range(2 * n):
		if s[i] == "0":
			result[i] = free_rows[introvert_index]
			occupied_rows[free_rows[introvert_index]].append(result[i])
			introvert_index += 1
			free_rows.pop(0)
		else:
			result[i] = occupied_rows[extrovert_index]
			free_rows[occupied_rows[extrovert_index]].append(result[i])
			extrovert_index += 1
			occupied_rows.pop(0)

	print(*result)


solve()
