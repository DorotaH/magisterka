grid = [input().strip() for _ in range(2)]
rotated = [grid[1][::-1], grid[0][::-1]]
if grid == rotated:
    print("YES")
else:
    print("NO")
