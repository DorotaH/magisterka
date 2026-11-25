import sys

# Read input from standard input
input_data = sys.stdin.read().strip()
# Split the input into individual side lengths
AB, BC, CA = map(int, input_data.split())

# Calculate the area of the right triangle
area = (AB * BC) // 2

# Print the area
print(area)
