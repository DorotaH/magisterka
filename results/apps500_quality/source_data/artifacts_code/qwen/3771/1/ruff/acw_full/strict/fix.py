def min_leaves_to_remove(H, W, grid):
	from collections import deque

	# Find the positions of S and T
	for i in range(H):
		for j in range(W):
			if grid[i][j] == 'S':
				start = (i, j)
			elif grid[i][j] == 'T':
				end = (i, j)

	# BFS to find the shortest path from S to T
	queue = deque([start])
	visited = set([start])
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	steps = 0

	while queue:
		for _ in range(len(queue)):
			x, y = queue.popleft()
			if (x, y) == end:
				return steps
			for dx, dy in directions:
				nx, ny = dx + x, dy + y
				if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and grid[nx][ny] != '.':
					visited.add((nx, ny))
					queue.append((nx, ny))
		steps += 1

	# If no path is found, it's not possible to reach T from S
	return -1


# Read input
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Output the result
print(min_leaves_to_remove(H, W, grid))
