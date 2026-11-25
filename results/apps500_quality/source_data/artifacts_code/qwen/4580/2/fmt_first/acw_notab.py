def min_max_colors(N, ratings):
    # Define the color ranges
    color_ranges = {
        "gray": (1, 399),
        "brown": (400, 799),
        "green": (800, 1199),
        "cyan": (1200, 1599),
        "blue": (1600, 1999),
        "yellow": (2000, 2399),
        "orange": (2400, 2799),
        "red": (2800, 3199),
    }

    # Initialize sets to keep track of used colors
    used_colors_min = set()
    used_colors_max = set()

    # Determine the minimum number of different colors
    for rating in ratings:
        found = False
        for color, (low, high) in color_ranges.items():
            if low <= rating <= high:
                used_colors_min.add(color)
                found = True
                break
        if not found:
            used_colors_min.add("custom")

    # Determine the maximum number of different colors
    used_colors_max.update(color_ranges.keys())
    if any(3200 <= rating for rating in ratings):
        used_colors_max.add("custom")

    # Output the results
    print(len(used_colors_min), len(used_colors_max))


# Read input
import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
ratings = list(map(int, data[1:]))

# Call the function
min_max_colors(N, ratings)
