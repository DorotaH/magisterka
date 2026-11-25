grid = [input().split() for _ in range(3)]

diagonal = "".join(grid[i][i] for i in range(0, 3))
print(diagonal)