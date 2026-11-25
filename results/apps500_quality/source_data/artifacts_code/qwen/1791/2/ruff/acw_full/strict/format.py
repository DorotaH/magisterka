def max_pile_size(s):
    n = len(s)
    max_size = 0

    # Try all possible fold positions
    for i in range(1, n):
        for j in range(i + 1, n):
            # Create the folded string
            folded = s[j:] + s[:i]
            # Check all possible piles
            for k in range(len(folded) - 1):
                pile = folded[k:]
                if all(pile[i] == pile[0] for i in range(1, len(pile))):
                    max_size = max(max_size, len(pile))

    return max_size


# Read input
s = input().strip()

# Print the result
print(max_pile_size(s))
