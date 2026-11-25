from collections import deque
from sys import stdin


def can_escape(n, m, grid):
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	visited = [[False] * m for _ in range(n)]
	queue = deque()

	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'G':
				queue.append((i, j, False))
				visited[i][j] = True

	while queue:
		x, y, bad = queue.popleft()

		for dx, dy in directions:
			nx, ny = dx + x, dy + y
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
				if grid[nx][ny] == 'B':
					queue.append((nx, ny, True))
				elif grid[nx][ny] in ['.', 'G']:
					queue.append((nx, ny, bad))
				visited[nx][ny] = True

	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'G':
				continue
			if grid[i][j] in ['.', 'B'] and not visited[i][j]:
				return False

	return True


t = int(stdin.readline())
for _ in range(t):
	n, m = map(int, stdin.readline().split())
	grid = [list(stdin.readline().strip()) for _ in range(n)]
	print("Yes" if can_escape(n, m, grid) else "No")
