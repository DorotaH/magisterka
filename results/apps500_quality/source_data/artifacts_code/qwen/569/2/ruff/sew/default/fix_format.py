def min_changes_to_distinct_substrings(s):
    n = len(s)
    max_unique_substrings = n * (n + 1) // 2
    unique_substrings = set()
    changes = 0

    for i in range(n):
        for j in range(1 + i, 1 + n):
            substring = s[i:j]
            if substring in unique_substrings:
                changes = changes + 1
                unique_substrings.remove(substring)
                s = s[0:i] + chr(ord(s[i]) + 1) + s[i + 1 :]
                substring = s[i:j]
            unique_substrings.add(substring)

    if len(unique_substrings) < max_unique_substrings:
        return -1
    return changes


# Read input
n = int(input())
s = input().strip()

# Print the result
print(min_changes_to_distinct_substrings(s))
