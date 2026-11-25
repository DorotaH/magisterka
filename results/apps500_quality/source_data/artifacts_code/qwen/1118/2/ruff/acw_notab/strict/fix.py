def min_turns_to_single_color(n, colors):
    # Find the most frequent color
    from collections import Counter
    color_count = Counter(colors)
    most_common_color = color_count.most_common(1)[0][0]
    most_common_count = color_count.most_common(1)[0][1]

    # The minimum number of turns is the number of squares that are not the most common color
    return n - most_common_count


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
colors = list(map(int, data[1:]))

# Output the result
print(min_turns_to_single_color(n, colors))
