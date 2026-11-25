def min_turns_to_single_color(n, colors):
    # Find the most frequent color in the list
    from collections import Counter

    color_count = Counter(colors)
    most_common_color, _ = color_count.most_common(1)[0]

    return sum(bool(color != most_common_color)
           for color in colors)


# Read input
n = int(input())
colors = list(map(int, input().split()))

# Output the result
print(min_turns_to_single_color(n, colors))
