from collections import deque


def bfs(grid, start, speed, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.' or 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny].isdigit() and int(grid[nx][ny]) == speed:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return sum(1 for row in visited for cell in row if cell)


def solve():
    n, m, p = map(int, input().split())
    speeds = list(map(int, input().split()))
    grid = [input().strip() for _ in range(n)]

    controlled_cells = [0] * (1 + p)

    for i in range(1, 1 + p):
        for j in range(n):
            for k in range(m):
                if grid[j][k] == str(i):
                    controlled_cells[i] += bfs(grid, (j, k), speeds[i - 1], n, m)

    print(" ".join(map(str, controlled_cells[1:])))


solve()
