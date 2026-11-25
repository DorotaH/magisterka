import  sys

def  read_input():
    n=int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    return  (n, grid)

def  calculate_magic_sum(grid):
    n=len(grid)
    magic_sum=sum(grid[i][i] for i in range(n))
    for i in range(0, n):
        magic_sum+=sum(grid[i])-grid[i][i]
    for i in range(0, n):
        magic_sum+=sum(grid[j][i] for j in range(n))-grid[i][i]
    magic_sum-=grid[n-1][n-1]
    return  magic_sum

def  find_magic_number(n, grid):
    magic_sum=calculate_magic_sum(grid)
    for i in range(0, n):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j]=magic_sum-(
                    sum(grid[i])-grid[i][i]+sum(grid[j])-grid[i][j]
                    )
                if calculate_magic_sum(grid)==magic_sum:
                    return  grid[i][j]
                grid[i][j]=0
    return  -1

def  main():
    n, grid=read_input()
    result=find_magic_number(n, grid)
    if not result != -1:
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    main()
