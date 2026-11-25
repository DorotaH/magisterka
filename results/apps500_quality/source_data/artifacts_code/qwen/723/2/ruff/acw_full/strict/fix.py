import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of friends
n = int(data[0])

# List to store the dimensions of the rectangles
rectangles = []

# Read the dimensions of each rectangle
for i in range(n):
	w = int(data[i * 2 + 1])
	h = int(data[i * 2 + 2])
	rectangles.append((w, h))

# Sort rectangles by width and height
rectangles.sort()

# Initialize the minimum area to a large number
min_area = float('inf')

# Try all possible orientations for each rectangle
for i in range(n):
	w, h = rectangles[i]
	# Calculate the width of the photo if the current rectangle is standing
	photo_width = sum(rectangles[j][0] for j in range(n) if j != i)
	# Calculate the height of the photo if the current rectangle is standing
	photo_height = max(rectangles[j][1] for j in range(n) if j != i)
	# Update the minimum area if the current configuration is smaller
	min_area = min(min_area, photo_width * (h + photo_height - h))
	# Calculate the width of the photo if the current rectangle is lying
	photo_width = sum(rectangles[j][1] for j in range(n) if j != i)
	# Calculate the height of the photo if the current rectangle is lying
	photo_height = max(rectangles[j][0] for j in range(n) if j != i)
	# Update the minimum area if the current configuration is smaller
	min_area = min(min_area, photo_width * (photo_height + w - w))

# Print the minimum area
print(min_area)
