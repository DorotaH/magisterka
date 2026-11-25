import sys

# Read input from standard input
A, B = map(int, sys.stdin.readline().split())

# Check if both numbers are between 1 and 9 (inclusive)
if 1 <= A <= 9 and 1 <= B <= 9:
	# Calculate the product
	result = B * A
	# Print the result
	print(result)
else:
	# Print -1 if the numbers are not between 1 and 9
	print(-1)
