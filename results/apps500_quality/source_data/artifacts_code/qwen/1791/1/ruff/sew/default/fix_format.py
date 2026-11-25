def find_largest_pile(s):
    n, max_pile = len(s), 0

    for i in range(n):
        for j in range(2 + i, n, 2):
            pile = s[i:j]
            if pile == pile[::-1]:
                max_pile = max(max_pile, len(pile))

    return max_pile


# Read input
import sys

input = sys.stdin.read
data = input().strip()

# Get the result
result = find_largest_pile(data)

# Print the result
print(result)
