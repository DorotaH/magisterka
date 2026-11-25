# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input data
H, W = int(data[0]), int(data[1])
h, w = int(data[2]), int(data[3])

# Calculate the number of remaining white cells
remaining_cells = ((H - h) * W) + ((W - w) * h)

# Print the result
print(remaining_cells)