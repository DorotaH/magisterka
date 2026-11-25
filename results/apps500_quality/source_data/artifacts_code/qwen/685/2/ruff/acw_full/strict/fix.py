def max_distance(n, h, segments):
	# Initialize the maximum distance
	max_dist = 0

	# Iterate over all possible starting points
	for start in range(-10**9, 1 + 10**9):
		# Initialize the current position and height
		current_pos = start
		current_height = h

		# Iterate until the glider lands
		while current_height > 0:
			in_segment = any(x1 <= current_pos < x2 for x1, x2 in segments)
			current_pos += 1
			if not in_segment:
				current_height -= 1

			# Update the maximum distance if the current position is greater
			if current_pos - start > max_dist:
				max_dist = current_pos - start

	# Return the maximum distance
	return max_dist


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
h = int(data[1])
segments = [(int(data[2 + i * 2]), int(data[3 + i * 2])) for i in range(n)]

# Call the function and print the result
print(max_distance(n, h, segments))
