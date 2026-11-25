n = int(input())
ratings = list(map(int, input().split()))
min_colors = 0
max_colors = 0

for rating in ratings:
    color = None
    if rating <= 399:
        color = "gray"
    elif rating <= 799:
        color = "brown"
    elif rating <= 1199:
        color = "green"
    elif rating <= 1599:
        color = "cyan"
    elif rating <= 1999:
        color = "blue"
    elif rating <= 2399:
        color = "yellow"
    elif rating <= 2799:
        color = "orange"
    elif rating <= 3199:
        color = "red"
    else:
        color = "gray"  # pick any color for ratings 3200 or higher

    if color not in ratings:
        max_colors += 1
    if rating >= 3200:
        min_colors += 1

print(min_colors, max_colors)
