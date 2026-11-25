def min_changes_to_distinct_substrings(n, s):
    if  n>26:
        return  -1

    count=26 * [0]
    for char in s:
        count[ord(char) - ord('a')] += 1

    changes=0
    for c in count:
        if  c > 1:
            changes += c - 1

    return  changes

# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(min_changes_to_distinct_substrings(n, s))
