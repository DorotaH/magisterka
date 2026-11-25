def can_solve_rubik_cube():
	# Read input
	import sys
	input = sys.stdin.read
	data = input().split()
	colors = list(map(int, data))

	# Count occurrences of each color
	color_count = [0] * 7
	for color in colors:
		color_count[color] += 1

	# Check if each color appears exactly 4 times
	if any(count != 4 for count in color_count[1:]):
		return "NO"

	# Create a 2D representation of the cube
	cube = [
		[colors[0], colors[1], colors[2], colors[3]],
		[colors[4], colors[5], colors[6], colors[7]],
		[colors[8], colors[9], colors[10], colors[11]],
		[colors[12], colors[13], colors[14], colors[15]],
		[colors[16], colors[17], colors[18], colors[19]],
		[colors[20], colors[21], colors[22], colors[23]]
	]

	# Check if the cube can be solved by rotating one face
	for i in range(6):
		# Rotate the i-th face 90 degrees clockwise
		rotated_face = [
			cube[i][3], cube[i][0], cube[i][1], cube[i][2]
		]
		# Check if the rotated face matches the opposite face
		opposite_face = [
			cube[(i + 3) % 6][0], cube[(i + 3) % 6][1], cube[(i + 3) % 6][2], cube[(i + 3) % 6][3]
		]
		if rotated_face == opposite_face:
			return "YES"

	return "NO"


# Call the function and print the result
print(can_solve_rubik_cube())
