def min_replacements(s, t):
    n, m = len(s), len(t)
    replacements = []
    for i in range(n):
        if s[i] != t[i]:
            replacements.append(i + 1)
    return len(replacements), replacements

# Read input
n, m = map(int, input().split())
s = input().strip()
t = input().strip()

# Get the result
k, replacements = min_replacements(s, t)

# Print the result
print(k)
print(' '.join(map(str, replacements)))
