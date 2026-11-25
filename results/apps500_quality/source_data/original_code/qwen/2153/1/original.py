def min_discrete_jumps(n, heights):
    jumps = 0
    i = 0
    while i < n - 1:
        max_height = max(heights[i+1:])
        min_height = min(heights[i+1:])
        if max_height < heights[i] or min_height > heights[i]:
            jumps += 1
            i += 1
        else:
            i = heights.index(max_height, i+1) + 1
    return jumps

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
heights = list(map(int, data[1:]))

# Calculate and print the result
result = min_discrete_jumps(n, heights)
print(result)
