def min_stones_to_place(S):
    n = len(S)
    black_count = S.count("B")
    white_count = S.count("W")

    return 0 if black_count == 0 or white_count == 0 else 1


# Read input from standard input
import sys

S = sys.stdin.read().strip()

# Print the result
print(min_stones_to_place(S))
