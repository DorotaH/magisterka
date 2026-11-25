import math


def min_performance(a, b, c, d):
    """Return the minimum duration of the performance."""
    # Calculate the maximum of the differences between the ropewalkers
    max_diff = max(abs(a - b), abs(b - c), abs(a - c))

    return max(0, 2 * math.ceil((max_diff - d) / 2))


# Read input from standard input
a, b, c, d = map(int, input().split())

# Print the result to standard output
print(min_performance(a, b, c, d))
