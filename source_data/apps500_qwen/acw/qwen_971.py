def is_convex(grid):
	n, m = len(grid), len(grid[0])
	black_cells = []

	# Find all black cells
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'B':
				black_cells.append((i, j))

	# If there is only one black cell, the grid is convex
	if len(black_cells) == 1:
		return "YES"

	# Check if the grid is convex
	def is_path_valid(path):
		for i in range(len(path) - 1):
			if abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1]) > 1:
				return False
		return True

	for i in range(len(black_cells)):
		for j in range(i + 1, len(black_cells)):
			path1 = [black_cells[i]]
			path2 = [black_cells[j]]
			if not is_path_valid(path1) or not is_path_valid(path2):
				return "NO"
			for k in range(len(black_cells)):
				if k not in [i, j]:
					path1.append(black_cells[k])
					path2.append(black_cells[k])
					if not is_path_valid(path1) or not is_path_valid(path2):
						return "NO"
					path1.pop()
					path2.pop()

	return "YES"


# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Output the result
print(is_convex(grid))
