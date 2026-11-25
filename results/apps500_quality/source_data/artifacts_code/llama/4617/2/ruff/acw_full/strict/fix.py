grid = [input() for _ in range(2)]


def rotate(grid):
	return [''.join(reversed(row)) for row in zip(*grid[::-1])]


rotated_grid = rotate(grid)
if grid == rotated_grid:
	print('YES')
else:
	print('NO')
