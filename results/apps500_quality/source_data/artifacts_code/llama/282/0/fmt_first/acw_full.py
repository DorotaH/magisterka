from collections import deque


def min_jumps(n, d, s):
	queue = deque([(1, 0)])
	visited = set([1])

	while queue:
		x, steps = queue.popleft()

		if x == n:
			return steps

		for jump in range(1, min(d, x) + 1):
			if jump + x <= n and s[jump + x] == "1" and (jump + x) not in visited:
				queue.append((jump + x, steps + 1))
				visited.add(jump + x)

	return -1


n, d = map(int, input().split())
s = input()

print(min_jumps(n, d, s))
