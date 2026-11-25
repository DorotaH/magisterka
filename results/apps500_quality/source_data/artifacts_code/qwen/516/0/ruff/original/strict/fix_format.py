def min_replacements(s, t):
    n, m = len(s), len(t)
    positions = []
    for i in range(n):
        if s[i] != t[i] and s[i] != "?":
            positions.append(i + 1)
    return len(positions), positions


# Read input
n, m = map(int, input().split())
s = input().strip()
t = input().strip()

# Get the result
k, positions = min_replacements(s, t)

# Print output
print(k)
print(" ".join(map(str, positions)))
