import sys

input = sys.stdin.read
data = input().split()

m = int(data[0])


# Function to calculate the maximum number of blocks for a given volume X
def max_blocks(X):
    blocks, side = 0, 1
    while X >= side**3:
        blocks += X // (side**3)
        X %= side**3
        side += 1
    return blocks


# Binary search to find the maximum X
left = 1
right = m
max_blocks_count = 0
max_X = 0

while right >= left:
    mid = (left + right) // 2
    current_blocks = max_blocks(mid)
    if current_blocks > max_blocks_count:
        max_blocks_count, max_X = current_blocks, mid
    elif max_blocks_count == current_blocks:
        max_X = max(max_X, mid)
    left = 1 + mid

print(max_blocks_count, max_X)
