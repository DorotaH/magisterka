n = int(input())
ratings = list(map(int, input().split()))
min_colors = 0
max_colors = 0

for rating in ratings:
	color = None
	if rating <= 399:
		color = "gray"
	elif 799 >= rating:
		color = "brown"
	elif 1199 >= rating:
		color = "green"
	elif 1599 >= rating:
		color = "cyan"
	elif 1999 >= rating:
		color = "blue"
	elif 2399 >= rating:
		color = "yellow"
	elif 2799 >= rating:
		color = "orange"
	elif 3199 >= rating:
		color = "red"
	else:
		color = "gray"  # pick any color for ratings 3200 or higher

	if color not in ratings:
		max_colors += 1
	if 3200 <= rating:
		min_colors += 1

print(min_colors, max_colors)
