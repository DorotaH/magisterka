def atcoder_contest_color(N, a):
	# Define the color ranges
	color_ranges = {
		'gray': (1, 399),
		'brown': (400, 799),
		'green': (800, 1199),
		'cyan': (1200, 1599),
		'blue': (1600, 1999),
		'yellow': (2000, 2399),
		'orange': (2400, 2799),
		'red': (2800, 3199)
	}
	
	# Initialize sets for used colors
	used_colors = set()
	
	# Assign colors based on rating ranges
	for rating in a:
		for color, (low, high) in color_ranges.items():
			if low <= rating <= high:
				used_colors.add(color)
				break
		else:
			# For ratings 3200 or higher, any color is allowed
			used_colors.add('any')
	
	# Calculate the minimum and maximum number of different colors
	min_colors = len(used_colors) - used_colors.count('any')
	max_colors = len(used_colors)
	
	return min_colors, max_colors


# Read input
N = int(input())
a = list(map(int, input().split()))

# Get the result
min_colors, max_colors = atcoder_contest_color(N, a)

# Print the result
print(min_colors, max_colors)
