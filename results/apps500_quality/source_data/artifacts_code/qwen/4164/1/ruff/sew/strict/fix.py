import math
import sys

# Read input from standard input
r = int(sys.stdin.read().strip())

# Calculate the area of the circle with radius r
area_r = math.pi * (r ** 2)

# Calculate the area of the circle with radius 1
area_1 = math.pi * (1 ** 2)

# Calculate the ratio of the areas
ratio = area_r / area_1

# Print the ratio as an integer
print(int(ratio))
