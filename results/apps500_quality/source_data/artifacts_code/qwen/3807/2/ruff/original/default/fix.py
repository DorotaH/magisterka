import sys

input = sys.stdin.read
data = input().split()

m = int(data[0])

# Function to calculate the maximum number of blocks for a given volume X
def max_blocks(X):
    blocks = 0
    side = 1
    while X >= side**3:
        blocks += X // side**3
        X %= side**3
        side += 1
    return blocks

# Binary search to find the maximum X
left, right = 1, m
max_blocks_count = 0
max_X = 0

while left <= right:
    mid = (left + right) // 2
    current_blocks = max_blocks(mid)
    if current_blocks > max_blocks_count:
        max_blocks_count = current_blocks
        max_X = mid
    elif current_blocks == max_blocks_count:
        max_X = max(max_X, mid)
    left = mid + 1

print(max_blocks_count, max_X)
