import sys

input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])

grid = [list(data[i + 2]) for i in range(H)]


def can_reach(start, end):
	queue = [start]
	visited = set()
	visited.add(start)

	while queue:
		x, y = queue.pop(0)
		if (x, y) == end:
			return True
		for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nx, ny = dx + x, dy + y
			if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and grid[nx][ny] != '.':
				visited.add((nx, ny))
				queue.append((nx, ny))

	return False


start = None
end = None
for i in range(H):
	for j in range(W):
		if grid[i][j] == 'S':
			start = (i, j)
		elif grid[i][j] == 'T':
			end = (i, j)

if not can_reach(start, end):
	print(-1)
	exit()


def dfs(x, y, visited):
	visited.add((x, y))
	for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		nx, ny = dx + x, dy + y
		if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and grid[nx][ny] != '.':
			dfs(nx, ny, visited)


def count_leaves_to_remove():
	visited = set()
	dfs(start[0], start[1], visited)
	dfs(end[0], end[1], visited)
	return len(visited) - 2


print(count_leaves_to_remove())
