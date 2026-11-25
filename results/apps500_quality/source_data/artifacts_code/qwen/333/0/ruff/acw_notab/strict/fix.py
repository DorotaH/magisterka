def longest_uncommon_subsequence(a, b):
    return -1 if a == b else max(len(a), len(b))


# Read input
a = input().strip()
b = input().strip()

# Output the result
print(longest_uncommon_subsequence(a, b))
