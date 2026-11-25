import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
W, H = int(data[0]), int(data[1])
x, y = int(data[2]), int(data[3])

# Calculate the maximum possible area of the part whose area is not larger than that of the other
max_area = min(x * H, (W - x) * H, y * W, W * (H - y))

# Check if there are multiple ways to cut the rectangle and achieve that maximum
if max_area == x * H == W * y:
    multiple_ways = 1
else:
    multiple_ways = 0

# Print the result
print(f"{max_area}.000000 {multiple_ways}")
