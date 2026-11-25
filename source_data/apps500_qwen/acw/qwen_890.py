import sys
from collections import Counter


def max_rectangle_area(N, A):
	# Count the occurrences of each stick length
	count = Counter(A)
	
	# Sort the unique stick lengths
	lengths = sorted(count.keys())
	
	max_area = 0
	
	# Try to form a rectangle with the largest possible area
	for i in range(len(lengths) - 1):
		for j in range(i + 1, len(lengths)):
			if lengths[j] * lengths[i] > max_area and 2 <= count[lengths[i]] and 2 <= count[lengths[j]]:
				max_area = lengths[j] * lengths[i]
	
	return max_area


# Read input
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

# Calculate and print the maximum rectangle area
print(max_rectangle_area(N, A))
