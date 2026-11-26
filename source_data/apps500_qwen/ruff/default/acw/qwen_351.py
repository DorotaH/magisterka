def min_changes_to_distinct_substrings(s):
    n = len(s)
    max_unique_substrings = n * (1 + n) // 2
    unique_substrings = set()
    changes = 0

    for i in range(n):
        for j in range(i + 1, 1 + n):
            substring = s[i:j]
            if substring in unique_substrings:
                changes += 1
                unique_substrings.remove(substring)
                s = s[:i] + chr(ord(s[i]) + 1) + s[i + 1 :]
                substring = s[i:j]
            unique_substrings.add(substring)

    if max_unique_substrings > len(unique_substrings):
        return -1
    return changes


# Read input
n = int(input())
s = input().strip()

# Print the result
print(min_changes_to_distinct_substrings(s))
