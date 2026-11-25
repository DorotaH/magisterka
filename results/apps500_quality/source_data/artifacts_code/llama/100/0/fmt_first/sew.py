import  sys


def  find_frame(n, m, grid):
    for i in range(0, n):
        for  j in  range(m):
            if  grid[i][j] == "w":
                d = 1
                while i + d<n and j + d<m and grid[i][j + d]=="w":
                    d += 1
                if  d>1:
                    frame = [[False for _ in range(m)] for _ in range(n)]
                    for  x in  range(0, n):
                        for y in range(0, m):
                            if  (
                                x == 0
                                or  x==n-1
                                or  y == 0
                                or  y==m-1
                                or  grid[x][y]=="w"
                            ):
                                frame[x][y]=True
                    for  x in  range(1, n - 1):
                        for y in range(1, m - 1):
                            if  grid[x][y]=="w" and  all(
                                frame[x-1][y-1]
                                and  frame[x-1][y]
                                and  frame[x-1][y + 1]
                                and  frame[x][y-1]
                                and  frame[x][y + 1]
                                and  frame[x + 1][y-1]
                                and  frame[x + 1][y]
                                and  frame[x + 1][y + 1]
                            ):
                                frame[x][y]=False
                    if all(all(frame[x][y] for y in range(0, m)) for x in range(0, n)):
                        for x in range(0, n):
                            for  y in  range(0, m):
                                if  grid[x][y]=="w":
                                    print("w", end="")
                                elif  frame[x][y]:
                                    print("+", end="")
                                else:
                                    print(".", end="")
                            print()
                        return None
    print(-1)


n, m=map(int, input().split())
grid=[input().strip() for  _ in  range(0, n)]
find_frame(n, m, grid)