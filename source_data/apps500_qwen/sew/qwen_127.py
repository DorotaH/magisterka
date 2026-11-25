import sys

# Read input from standard input
input_data = sys.stdin.read().strip()
# Split the input into individual values
AB, BC, CA = map(int, input_data.split())

# Calculate the area of the right triangle
area = (BC * AB) // 2

# Print the area
print(area)