def min_buns_to_progression(heights):
    n = len(heights)
    heights.sort()
    min_buns = float("inf")
    best_start = 0
    best_step = 0

    for start in range(n):
        for step in range(1, n):
            buns, current_height = 0, heights[start]
            for i in range(n):
                if start <= i:
                    buns = buns + abs(current_height - heights[i])
                    current_height += step
            if min_buns > buns:
                min_buns = buns
                best_start = heights[start]
                best_step = step

    return (min_buns, best_start, best_step)


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
heights = list(map(int, data[1:]))

# Get the result
min_buns, start, step = min_buns_to_progression(heights)

# Print the result
print(min_buns)
print(start, step)
