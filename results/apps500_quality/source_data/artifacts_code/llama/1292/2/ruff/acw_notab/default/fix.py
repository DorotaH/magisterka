from collections import deque


def canExpand(grid, x, y, s, player):
    n, m = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), 1, -1]
    queue = deque([(x, y)])
    visited = {(x, y)}
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if nx + dx <= x + s or dy + ny <= y + s:
                    return True
    return False


def expand(grid, s, player):
    n, m = len(grid), len(grid[0])
    new_grid = [list(row) for row in grid]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.' and canExpand(grid, i, j, s, player):
                new_grid[i][j] = str(player)
    return new_grid


def solve(grid, s):
    n, m = len(grid), len(grid[0])
    new_grid = [list(row) for row in grid]
    players = [0] * 10
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                players[int(grid[i][j])] += 1
    while True:
        new_players = [0] * 10
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '.':
                    new_players[int(grid[i][j])] += 1
        for p in range(1, 10):
            new_grid = expand(new_grid, s[p - 1], p)
        if new_players == list(new_grid[0]):
            break
        grid = [row[:] for row in new_grid]
    return new_players[1:]


n, m, p = map(int, input().split())
s = list(map(int, input().split()))
grid = [list(input().strip()) for _ in range(n)]
print(*solve(grid, s))
