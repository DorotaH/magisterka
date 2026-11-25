N = int(input())
ratings = list(map(int, input().split()))
colors = ["gray", "brown", "green", "cyan", "blue", "yellow", "orange", "red"]
min_colors, max_colors = set(), set()

for rating in ratings:
    if rating <= 399:
        min_colors.add("gray")
    elif rating <= 799:
        min_colors.add("brown")
    elif rating <= 1199:
        min_colors.add("green")
    elif rating <= 1599:
        min_colors.add("cyan")
    elif rating <= 1999:
        min_colors.add("blue")
    elif rating <= 2399:
        min_colors.add("yellow")
    elif rating <= 2799:
        min_colors.add("orange")
    elif rating <= 3199:
        min_colors.add("red")

    max_colors.add(colors[(rating - 1) % 8])

print(len(min_colors), len(max_colors))
