# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input data
H = int(data[0])
W = int(data[1])
h = int(data[2])
w = int(data[3])

# Calculate the number of remaining white cells
remaining_cells = W * (H - h) + h * (W - w)

# Print the result
print(remaining_cells)
