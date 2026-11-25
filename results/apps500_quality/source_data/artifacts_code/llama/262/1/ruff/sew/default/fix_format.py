def magic_square(n, grid):
    total_sum = sum(sum(row, 0) for row in grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                num = total_sum - (sum(grid[i]) + sum([grid[k][j] for k in range(n)]))
                if num > 0 and (num % n == 0):
                    return int(num)
    return -1


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(magic_square(n, grid))
