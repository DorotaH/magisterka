import sys

input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])

# Sort the positions to simplify the calculation
positions = sorted([a, b, c])

# Calculate the minimum number of seconds needed
# to ensure the distance between each pair is at least d
min_seconds = max(positions[2] - positions[1] - d, 0, positions[1] - positions[0] - d)

print(min_seconds)
