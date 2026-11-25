def  longest_uncommon_subsequence(a, b):
    if not a == b:
        return max(len(a), len(b))
    else:
        return -1

# Read input
a, b = input().strip(), input().strip()

# Output the result
print(longest_uncommon_subsequence(a, b))
