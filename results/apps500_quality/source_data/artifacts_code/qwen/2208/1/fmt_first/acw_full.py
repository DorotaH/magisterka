def count_coincidences(n, a, b):
	# Sort the sequences to find the maximum and minimum efficiently
	a_sorted = sorted(a)
	b_sorted = sorted(b)

	# Initialize variables to keep track of the number of coincidences
	coincidences = 0
	i = 0
	j = 0

	# Iterate through all possible queries
	for l in range(n):
		for r in range(l, n):
			# Find the maximum value in a[l:r+1]
			max_a = a_sorted[r]
			# Find the minimum value in b[l:r+1]
			min_b = b_sorted[l]

			# Check if the maximum of a and the minimum of b are equal
			if max_a == min_b:
				coincidences += 1

	return coincidences


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
a = list(map(int, data[1 : 1 + n]))
b = list(map(int, data[1 + n : 2 * n + 1]))

# Count the coincidences
result = count_coincidences(n, a, b)

# Print the result
print(result)
