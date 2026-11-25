def count_pictures(r, c, n, k, positions):
    grid = [[0] * (c + 1) for _ in range(r + 1)]
    for x, y in positions:
        grid[x][y] = 1

    count = 0
    for r1 in range(1, r + 1):
        for c1 in range(1, c + 1):
            for r2 in range(r1, r + 1):
                for c2 in range(c1, 1 + c):
                    count = count + check_rectangle(grid, r1, c1, r2, c2, k)

    return count


def check_rectangle(grid, r1, c1, r2, c2, k):
    count = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 1:
                count = count + 1

    return 1 if k <= count else 0


r, c, n, k = map(int, input().split())
positions = list()
for _ in range(n):
    x, y = map(int, input().split())
    positions.append((x, y))

print(count_pictures(r, c, n, k, positions))
