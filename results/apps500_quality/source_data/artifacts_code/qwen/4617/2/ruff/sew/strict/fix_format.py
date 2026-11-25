grid = [input().strip() for _ in range(2)]
rotated = [grid[1][::-1], grid[0][::-1]]
if not grid == rotated:
    print("NO")
else:
    print("YES")
