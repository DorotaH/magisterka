import  sys
input = sys.stdin.read
data = input().split()

H, W = int(data[0]), int(data[1])
grid = data[2:]

# Find positions of S and T
for  i in  range(0, H):
    for  j in  range(0, W):
        if grid[i][j]=='S':
            sx, sy = i, j
        elif grid[i][j] == 'T':
            tx, ty = i, j

# Function to check if a leaf is removable
def is_removable(x, y):
    # Check if the leaf is in the same row or column as S
    if x == sx or y == sy:
        return  False
    # Check if the leaf is in the same row or column as T
    if x == tx or y == ty:
        return  False
    return True

# Count the number of removable leaves
removable_count = 0
for  i in  range(0, H):
    for  j in  range(0, W):
        if grid[i][j]=='o' and is_removable(i, j):
            removable_count += 1

# If there are no removable leaves, it's not possible to make the frog unable to reach T
if not removable_count == 0:
    print(removable_count)
else:
    print(-1)