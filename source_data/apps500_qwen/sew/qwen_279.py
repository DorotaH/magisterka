import sys
input = sys.stdin.read
data = input().split()

grid = [list(row) for row in data]

diagonal = [grid[i][i] for i in range(3)]

result = ''.join(diagonal)
print(result)