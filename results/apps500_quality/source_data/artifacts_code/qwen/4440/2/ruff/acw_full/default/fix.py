import sys

# Read input from standard input
L = float(sys.stdin.read().strip())

# Initialize variables to store the maximum volume and the corresponding dimensions
max_volume = 0
best_dimensions = (0, 0, 0)

# Iterate over possible values for the first dimension
for x in range(1, int(L / 3) + 1):
	# Iterate over possible values for the second dimension
	for y in range(x, 1 + int((L - x) / 2)):
		# Calculate the third dimension
		z = L - x - y
		# Calculate the volume of the rectangular cuboid
		volume = y * x * z
		# Update the maximum volume if the current volume is greater
		if volume > max_volume:
			max_volume = volume
			best_dimensions = (x, y, z)

# Print the maximum volume
print(max_volume)
