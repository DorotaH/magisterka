def min_extensions(a, b, h, w, n, extensions):
	# Check if the rectangle can fit in the initial field
	if a <= h and w >= b:
		return 0
	
	# Check if the rectangle can fit by swapping dimensions
	if h >= b and a <= w:
		return 0
	
	# Sort extensions to try the smallest multipliers first
	extensions.sort()
	
	# Try using extensions to increase the dimensions
	for i in range(n):
		if a <= extensions[i] * h and w >= b:
			return i + 1
		if b <= extensions[i] * h and a <= w:
			return i + 1
	
	# If no extension can fit the rectangle, return -1
	return -1


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
a = int(data[0])
b = int(data[1])
h = int(data[2])
w = int(data[3])
n = int(data[4])
extensions = list(map(int, data[5:]))

# Output the result
print(min_extensions(a, b, h, w, n, extensions))
