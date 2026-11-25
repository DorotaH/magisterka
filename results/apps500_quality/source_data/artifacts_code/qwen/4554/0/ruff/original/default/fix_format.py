# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Extract the values of W, a, and b
W = int(data[0])
a = int(data[1])
b = int(data[2])

# Calculate the minimum distance the second rectangle needs to be moved
# The minimum distance is the difference between the leftmost points of the two rectangles
min_distance = abs(a - b)

# Print the minimum distance
print(min_distance)
