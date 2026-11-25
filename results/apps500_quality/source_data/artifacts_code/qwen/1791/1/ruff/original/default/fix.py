def find_largest_pile(s):
    n = len(s)
    max_pile = 0

    for i in range(n):
        for j in range(i + 2, n, 2):
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
