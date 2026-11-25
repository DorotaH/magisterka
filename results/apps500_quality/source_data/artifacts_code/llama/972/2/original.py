from collections import deque

def is_convex(grid):
    n, m = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        queue = deque([(i, j)])
        grid[i][j] = '.'

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'B'):
                    grid[nx][ny] = '.'
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                dfs(i, j)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                count = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if (0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.'):
                        count += 1
                if count > 2:
                    return 'NO'

    return 'YES'

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

print(is_convex(grid))
