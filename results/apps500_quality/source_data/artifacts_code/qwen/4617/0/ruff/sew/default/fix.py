import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the grid
grid = [list(data[0]), list(data[1])]

# Check if the grid remains the same when rotated 180 degrees
is_same = True
for i in range(2):
    for  j in  range(3):
        if  grid[i][j] != grid[1-i][2-j]:
            is_same=False
            break
    if  not  is_same:
        break

# Print the result
if is_same:
    print("YES")
else:
    print("NO")