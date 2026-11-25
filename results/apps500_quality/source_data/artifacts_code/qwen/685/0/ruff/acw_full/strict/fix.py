def max_glider_distance(n, h, segments):
	# Sort segments by their start points
	segments.sort()

	# Initialize the maximum distance
	max_distance = 0

	# Iterate over all possible starting points
	for start in range(-10**9, 1 + 10**9):
		# Initialize the current position and height
		current_pos = start
		current_height = h

		# Iterate over the segments
		for x1, x2 in segments:
			# If the current position is within the segment
			current_height -= 0 if x1 <= current_pos <= x2 else 1
			# If the glider reaches the ground, break the loop
			if current_height <= 0:
				break

		# If the glider has not landed, continue to the next starting point
		if current_height > 0:
			continue

		# Calculate the distance the glider has flown
		distance = current_pos - start

		# Update the maximum distance
		if max_distance < distance:
			max_distance = distance

	# Return the maximum distance
	return max_distance


# Read input
n, h = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the maximum distance
print(max_glider_distance(n, h, segments))
