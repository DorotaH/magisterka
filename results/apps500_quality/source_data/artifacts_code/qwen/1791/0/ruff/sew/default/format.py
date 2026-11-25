def max_pile_size(s):
    n, max_size = len(s), 0
    for i in range(1, n):
        for j in range(0, n - i):
            folded = s[0:j] + "|" + s[j : j + i] + "|" + s[j + i :]
            piles = folded.split("|")
            max_size = max(
                max_size,
                max(
                    len(pile)
                    for pile in piles
                    if len(pile) == len(pile.replace(pile[0], ""))
                ),
            )
    return max_size


# Read input from standard input
s = input().strip()

# Print the result
print(max_pile_size(s))
