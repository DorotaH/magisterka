def determine_winner(s):
    n = len(s)
    if n <= 2:
        return "First"

    return next(
        ("First" for i in range(1, n - 1) if s[i] not in [s[i - 1], s[i + 1]]),
        "Second",
    )


# Read input from standard input
import sys

s = sys.stdin.read().strip()

# Determine the winner and print the result
print(determine_winner(s))
