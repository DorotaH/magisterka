grid = [input(), input()]


def rotate_180(grid):
	return [list(reversed(row)) for row in reversed(grid)]


def is_same(grid, rotated_grid):
	for i in range(2):
		for j in range(3):
			if grid[i][j] != rotated_grid[i][j]:
				return False
	return True


rotated_grid = rotate_180(grid)
print("YES" if is_same(grid, rotated_grid) else "NO")
