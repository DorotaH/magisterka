grid = [input().split() for _ in range(3)]

print("".join(grid[i][i] for i in range(3)))
