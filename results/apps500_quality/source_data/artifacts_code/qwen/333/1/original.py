def longest_uncommon_subsequence(a, b):
    if a == b:
        return -1
    else:
        return max(len(a), len(b))

# Read input from standard input
import sys
input = sys.stdin.read
data = input().split()

# Get the strings
a = data[0]
b = data[1]

# Calculate and print the result
result = longest_uncommon_subsequence(a, b)
print(result)
