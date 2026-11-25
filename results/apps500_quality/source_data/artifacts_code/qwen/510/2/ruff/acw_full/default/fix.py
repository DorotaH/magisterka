def min_duration(a, b, c, d):
	# Sort the positions to simplify the calculation
	positions = sorted([a, b, c])
	return max(
		max(positions[2] - positions[1] - d, 0),
		max(positions[1] - positions[0] - d, 0),
	)


# Read input
a, b, c, d = map(int, input().split())

# Print the result
print(min_duration(a, b, c, d))
