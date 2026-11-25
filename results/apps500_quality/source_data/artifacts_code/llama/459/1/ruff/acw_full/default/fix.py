import sys


def check_cube(s):
	colors = [0, 0, 0, 0]
	for i in range(24):
		colors[s[i] - 1] += 1

	# Check if all colors have the same count
	for c in colors:
		if c != 4:
			return 'NO'

	# Check if each face has the same color
	for i in range(0, 6, 4):
		face_colors = sorted(s[i:i + 4])
		if face_colors not in [
			[1, 1, 1, 1],
			[2, 2, 2, 2],
			[3, 3, 3, 3],
			[4, 4, 4, 4],
			[5, 5, 5, 5],
			[6, 6, 6, 6],
		]:
			return 'NO'

	return next(
		(
			'YES'
			for i in range(6)
			if s[i] == s[i + 4]
			and s[i + 8] == s[i + 12]
			and s[i + 16] == s[20 + i]
			and s[i + 24] == s[i]
		),
		'NO',
	)


# Read input from standard input
input_str = sys.stdin.readline().strip()
s = list(map(int, input_str.split()))

print(check_cube(s))
