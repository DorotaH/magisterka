grid = [input().strip(), input().strip()]


def rotate_180(grid):
    return [''.join(reversed(x)) for x in zip(*grid[::-1])]


rotated_grid = rotate_180(grid)

if grid == rotated_grid:
    print('YES')
else:
    print('NO')
