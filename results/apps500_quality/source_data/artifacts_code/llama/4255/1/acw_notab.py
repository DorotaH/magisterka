import math
import sys

# Read input from standard input
a, b, c = map(int, input().split())

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Check if the input sides can form a triangle
if a + b > c and a + c > b and b + c > a:
    # Calculate the area using Heron's formula
    area = math.sqrt((s - a) * s * (s - b) * (s - c))
    # Print the area
    print(int(area))
else:
    # If the sides cannot form a triangle, print an error message
    print("Error: The given sides cannot form a triangle.")
