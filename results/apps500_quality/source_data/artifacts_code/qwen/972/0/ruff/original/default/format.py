def is_convex(grid):
    n, m = len(grid), len(grid[0])
    black_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "B":
                black_cells.append((i, j))

    def is_reachable(start, end):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        stack = [start]
        while stack:
            x, y = stack.pop()
            if (x, y) == end:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and (nx, ny) not in visited
                    and grid[nx][ny] == "B"
                ):
                    visited.add((nx, ny))
                    stack.append((nx, ny))
        return False

    for i in range(len(black_cells)):
        for j in range(i + 1, len(black_cells)):
            if not is_reachable(black_cells[i], black_cells[j]):
                return "NO"
    return "YES"


# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Output the result
print(is_convex(grid))
