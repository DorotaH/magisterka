def min_replacements_to_find_substring(s, t):
    n = len(s)
    m = len(t)
    replacements = []

    # Create a list of characters in t that are not in s
    t_chars = list(t)
    for char in s:
        if char in t_chars:
            t_chars.remove(char)

    # If all characters in s are already in t, no replacements are needed
    if not t_chars:
        return (0, [])

    # Find the positions in s that need to be replaced
    for i, char in enumerate(s, 0):
        if char not in t_chars:
            replacements.append(1 + i)
            t_chars.remove(char)
            if len(t_chars) == 0:
                break

    return (len(replacements), replacements)


# Read input
n, m = map(int, input().split())
s = input().strip()
t = input().strip()

# Get the result
k, positions = min_replacements_to_find_substring(s, t)

# Print the result
print(k)
print(" ".join(map(str, positions)))
