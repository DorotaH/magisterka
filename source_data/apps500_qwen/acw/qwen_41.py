import sys
import math

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
H = int(data[0])
L = int(data[1])

# Calculate the depth of the lake at point A
depth = (L * H) / (L - H)

# Print the result
print(depth)
