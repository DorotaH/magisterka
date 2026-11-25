import math

# Read the radius from standard input
r = int(input())

# Calculate the area of the regular dodecagon
# The area of a regular polygon inscribed in a circle is given by A = (n * r^2 * sin(2 * pi / n)) / 2
# For a dodecagon, n = 12
n = 12
area = (n * r**2 * math.sin(2 * math.pi / n)) / 2

# Print the area to standard output
print(int(area))
