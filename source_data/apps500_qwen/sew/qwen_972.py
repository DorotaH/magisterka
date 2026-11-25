def is_convex_grid(grid):
    n = len(grid)
    m = len(grid[0])
    black_cells=[(i, j) for  i in  range(0, n) for  j in  range(0, m) if  grid[i][j]=='B']
    if  len(black_cells) == 1:
        return "YES"
    
    directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
    for  i in  range(0, len(black_cells)):
        for  j in  range(1 + i, len(black_cells)):
            x1, y1 = black_cells[i]
            x2, y2 = black_cells[j]
            dx = x2 - x1
            dy = y2 - y1
            if abs(dx) + abs(dy) != 2:
                return  "NO"
            if not any((x1 + dx + dirs[0], y1 + dy + dirs[1]) in black_cells for dirs in directions):
                return  "NO"
    return "YES"

# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Output result
print(is_convex_grid(grid))