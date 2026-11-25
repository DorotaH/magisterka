import sys
import math

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse input
R = int(data[0])
x1, y1 = map(int, data[1:3])
x2, y2 = map(int, data[3:5])


# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Calculate the distance from the center of the flat to Fafa's laptop
d = distance(x1, y1, x2, y2)

# If Fafa's laptop is inside the flat, the optimal radius is the distance to Fafa's laptop
if R >= d:
	r = d
	x_ap = x2
	y_ap = y2
else:
	# If Fafa's laptop is outside the flat, the optimal radius is the distance to Fafa's laptop minus the radius of the flat
	r = d - R
	# The access point should be placed on the line connecting the center of the flat and Fafa's laptop
	# The coordinates of the access point are:
	x_ap = x1 + (x2 - x1) * (R / d)
	y_ap = y1 + (y2 - y1) * (R / d)

# Print the result
print(f"{x_ap} {y_ap} {r}")
