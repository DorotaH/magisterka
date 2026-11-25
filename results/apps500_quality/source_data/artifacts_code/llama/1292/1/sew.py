from collections import deque

def main():
    n, m, p=map(int, input().split())
    speed = list(map(int, input().split()))
    grid = [list(input().strip()) for _ in range(n)]
    def  get_neighbours(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                yield  (nx, ny)
    def  is_valid_move(grid, player, x, y):
        for dx, dy in get_neighbours(x, y):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or n <= nx or m <= ny or grid[nx][ny] != '.':
                return  False
        return  True
    def  expand(grid, player):
        queue=deque()
        for i in range(n):
            for  j in  range(m):
                if grid[i][j] == str(player):
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for nx, ny in get_neighbours(x, y):
                if grid[nx][ny] == '.' and is_valid_move(grid, player, nx, ny):
                    grid[nx][ny] = str(player)
                    queue.append((nx, ny))

    for _ in range(p):
        for  player in  range(1, 1 + p):
            expand(grid, player)

    print(' '.join(str(grid.count(str(i))) for  i in  range(1, 1 + p)))

if  __name__=='__main__':
    main()