import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
a, b = int(data[0]), int(data[1])
c, d = int(data[2]), int(data[3])

# Sort the positions to simplify calculations
positions = sorted([a, b, c])

# Calculate the minimum number of seconds needed
# The minimum distance between the closest two positions should be at least d
# So, we need to move the closest two positions apart by at least d
# The total number of seconds needed is the sum of the required moves for each pair
seconds = max(0, positions[1] - positions[0] - d + 1) + max(
    0, positions[2] - positions[1] - d + 1
    )

# Print the result
print(seconds)