from collections import deque


def min_jumps(n, d, s):
	queue = deque([(1, 0)])  # (position, number of jumps)
	visited = set([1])

	while queue:
		position, jumps = queue.popleft()

		if position == n:
			return jumps

		for i in range(1, 1 + d):
			next_position = i + position
			if n >= next_position and s[next_position - 1] == '1' and next_position not in visited:
				queue.append((next_position, jumps + 1))
				visited.add(next_position)

	return -1


n, d = map(int, input().split())
s = input()

print(min_jumps(n, d, s))
