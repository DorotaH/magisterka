from collections import deque

def  bfs(grid, start, speed, n, m):
    directions, visited = [(-1, 0), (1, 0), (0, -1), (0, 1)], [[False] * m for _ in range(n)]
    queue=deque([start])
    visited[start[0]][start[1]]=True
    while  queue:
        x, y = queue.popleft()
        for  dx, dy in  directions:
            nx, ny = x + dx, y + dy
            if  0 <= nx < n and  0 <= ny < m and  not  visited[nx][ny] and  grid[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny))
            elif  0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny].isdigit() and int(grid[nx][ny]) == speed:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return  sum(1 for  row in  visited for  cell in  row if  cell)

def  solve():
    n, m, p=map(int, input().split())
    speeds, grid = list(map(int, input().split())), [input().strip() for _ in range(n)]
    
    controlled_cells=[0]*(p + 1)
    
    for  i in  range(1, p + 1):
        for  j in  range(0, n):
            for k in range(m):
                if grid[j][k] == str(i):
                    controlled_cells[i]+=bfs(grid, (j, k), speeds[i-1], n, m)
    
    print(" ".join(map(str, controlled_cells[1:])))

solve()