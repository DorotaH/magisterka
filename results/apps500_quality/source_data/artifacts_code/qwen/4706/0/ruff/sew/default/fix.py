import sys

input = sys.stdin.read
data = input().split()
grid = [data[0], data[1], data[2]]
result = grid[0][0] + grid[1][1] + grid[2][2]
print(result)