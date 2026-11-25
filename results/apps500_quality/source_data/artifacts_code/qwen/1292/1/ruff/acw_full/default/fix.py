from collections import deque


def bfs(grid, n, m, player, s):
	visited = [[False] * m for _ in range(n)]
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque()
	
	for i in range(n):
		for j in range(m):
			if grid[i][j] == str(player):
				visited[i][j] = True
				queue.append((i, j, 0))
	
	while queue:
		x, y, dist = queue.popleft()
		if dist > s:
			break
		for dx, dy in directions:
			nx, ny = dx + x, dy + y
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
				visited[nx][ny] = True
				queue.append((nx, ny, dist + 1))
	
	return sum(row.count(str(player)) for row in grid)


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	n, m, p = map(int, data[:3])
	s = list(map(int, data[3:3 + p]))
	grid = data[3 + p:]

	result = [0] * p
	for player in range(1, 1 + p):
		result[player - 1] = bfs(grid, n, m, player, s[player - 1])

	print(' '.join(map(str, result)))


if __name__ == "__main__":
	main()
