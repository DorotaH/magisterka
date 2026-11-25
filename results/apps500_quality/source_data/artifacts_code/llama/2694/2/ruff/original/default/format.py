import sys


def dda(n, m, blasters):
    blasters.sort(key=lambda x: x[2])
    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = min(i + 1, m - j)

    for i in range(n):
        for j in range(m):
            for x, y, t, f in blasters:
                if (i, j) == (x, y):
                    return "NO"
                distance = max(abs(i - x), abs(j - y))
                if t <= grid[i][j]:
                    grid[i][j] = min(grid[i][j], distance)
                grid[i][j] = min(grid[i][j], grid[i][j] + 1)

    time = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] < time:
                return "NO"
            time = max(time, grid[i][j])

    return "YES\n" + str(time)


n, m, k = map(int, input().split())
blasters = []
for _ in range(k):
    x, y, t, f = map(int, input().split())
    blasters.append((x - 1, y - 1, t, f))

print(dda(n, m, blasters))
