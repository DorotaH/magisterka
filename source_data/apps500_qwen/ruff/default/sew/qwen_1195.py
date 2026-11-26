from collections import defaultdict


def min_max_colors(N, ratings):
    # Define the color ranges
    color_ranges = [
        (1, 399, "gray"),
        (400, 799, "brown"),
        (800, 1_199, "green"),
        (1_200, 1_599, "cyan"),
        (1_600, 1_999, "blue"),
        (2_000, 2_399, "yellow"),
        (2_400, 2_799, "orange"),
        (2_800, 3_199, "red"),
    ]

    # Create a dictionary to store the colors of users with ratings below 3200
    user_colors = defaultdict(str)

    # Assign colors to users based on their ratings
    for rating in ratings:
        if rating < 3_200:
            for start, end, color in color_ranges:
                if start <= rating <= end:
                    user_colors[rating] = color
                    break

    # The minimum number of different colors is the number of unique colors assigned
    min_colors = len(user_colors)

    # The maximum number of different colors is the total number of users plus the number of users with ratings 3200 or higher
    max_colors = N + sum(1 for rating in ratings if rating >= 3_200)

    return min_colors, max_colors


# Read input
N, ratings = int(input()), list(map(int, input().split()))

# Calculate and print the result
min_colors, max_colors = min_max_colors(N, ratings)
print(min_colors, max_colors)
