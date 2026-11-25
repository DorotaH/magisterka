import sys

# Read input
H, L = map(int, sys.stdin.readline().split())

# Calculate the depth of the lake
depth = H * L / (L - H)

# Print the result
print(depth)
