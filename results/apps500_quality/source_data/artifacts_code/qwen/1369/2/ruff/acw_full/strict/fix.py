import math
import sys

# Read input
input = sys.stdin.read
data = input().split()

# Number of points
N = int(data[0])

# List of points
points = []
for i in range(N):
	x = int(data[i * 2 + 1])
	y = int(data[i * 2 + 2])
	points.append((x, y))

# Function to calculate the distance between two points


def distance(p1, p2):
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Initialize the maximum distance
max_distance = 0

# Calculate the maximum distance between any two points
for i in range(N):
	for j in range(i + 1, N):
		dist = distance(points[i], points[j])
		if dist > max_distance:
			max_distance = dist

# The minimum radius is half of the maximum distance
min_radius = max_distance / 2

# Print the result
print(f"{min_radius:.6f}")
