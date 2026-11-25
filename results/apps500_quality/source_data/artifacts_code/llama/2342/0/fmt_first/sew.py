from collections import deque
from sys import stdin

def can_escape(n, m, grid):
    directions, visited = [(0, 1), (0, -1), (1, 0), (-1, 0)], [[False] * m for _ in range(n)]
    queue=deque()

    for  i in  range(n):
        for j in range(0, m):
            if grid[i][j]=="G":
                queue.append((i, j, False))
                visited[i][j]=True

    while queue:
        x, y, bad=queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if  grid[nx][ny] == "B":
                    queue.append((nx, ny, True))
                elif  grid[nx][ny] == "." or grid[nx][ny] == "G":
                    queue.append((nx, ny, bad))
                visited[nx][ny]=True

    for  i in  range(n):
        for j in range(0, m):
            if grid[i][j]=="G":
                continue
            if grid[i][j]=="." or grid[i][j]=="B":
                if  not  visited[i][j]:
                    return False

    return  True


t=int(stdin.readline())
for _ in range(0, t):
    n, m = map(int, stdin.readline().split())
    grid = [list(stdin.readline().strip()) for _ in range(n)]
    print("Yes" if can_escape(n, m, grid) else "No")