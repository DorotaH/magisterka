import sys

input = sys.stdin.read
data = input().split()

grid = [list(data[0]), list(data[1])]

rotated_grid = [row[::-1] for row in grid[::-1]]

if not grid == rotated_grid:
    print("NO")
else:
    print("YES")