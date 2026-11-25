from collections import deque


def is_possible(maze):
    n, m = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    queue = deque()
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                if maze[nx][ny] == '.':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif maze[nx][ny] == 'B':
                    return False

    return True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]
    print("Yes" if is_possible(maze) else "No")
