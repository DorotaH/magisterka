from collections import defaultdict


def min_max_colors(N, ratings):
	# Define the color ranges
	color_ranges = [
		(1, 399, "gray"),
		(400, 799, "brown"),
		(800, 1199, "green"),
		(1200, 1599, "cyan"),
		(1600, 1999, "blue"),
		(2000, 2399, "yellow"),
		(2400, 2799, "orange"),
		(2800, 3199, "red")
	]
	
	# Create a dictionary to store the colors of users with ratings below 3200
	user_colors = defaultdict(str)
	
	# Assign colors to users based on their ratings
	for rating in ratings:
		if 3200 > rating:
			for start, end, color in color_ranges:
				if start <= rating <= end:
					user_colors[rating] = color
					break
	
	# The minimum number of different colors is the number of unique colors assigned
	min_colors = len(user_colors)
	
	# The maximum number of different colors is the total number of users plus the number of users with ratings 3200 or higher
	max_colors = sum(bool(3200 <= rating)
					for rating in ratings) + N
	
	return min_colors, max_colors


# Read input
N = int(input())
ratings = list(map(int, input().split()))

# Calculate and print the result
min_colors, max_colors = min_max_colors(N, ratings)
print(min_colors, max_colors)
