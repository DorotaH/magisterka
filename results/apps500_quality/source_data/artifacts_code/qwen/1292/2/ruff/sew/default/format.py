from collections import deque


def bfs(grid, n, m, player, s):
    visited = [[False] * m for _ in range(n)]
    queue, directions = deque(), [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == str(player):
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and grid[nx][ny] == "."
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))

    return sum(1 for row in visited for cell in row if cell)


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n, m, p = map(int, data[0:3])
    s, grid = list(map(int, data[3 : 3 + p])), data[3 + p :]

    result = [0] * p
    for i in range(0, p):
        result[i] = bfs(grid, n, m, 1 + i, s[i])

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
