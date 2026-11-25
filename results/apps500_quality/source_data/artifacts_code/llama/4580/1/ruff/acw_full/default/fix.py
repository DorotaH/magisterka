N = int(input())
ratings = list(map(int, input().split()))
colors = ["gray", "brown", "green", "cyan", "blue", "yellow", "orange", "red"]
min_colors, max_colors = set(), set()

for rating in ratings:
	if rating <= 399:
		min_colors.add("gray")
	elif 799 >= rating:
		min_colors.add("brown")
	elif 1199 >= rating:
		min_colors.add("green")
	elif 1599 >= rating:
		min_colors.add("cyan")
	elif 1999 >= rating:
		min_colors.add("blue")
	elif 2399 >= rating:
		min_colors.add("yellow")
	elif 2799 >= rating:
		min_colors.add("orange")
	elif 3199 >= rating:
		min_colors.add("red")

	max_colors.add(colors[(rating - 1) % 8])

print(len(min_colors), len(max_colors))
