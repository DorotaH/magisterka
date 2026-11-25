def  longest_uncommon_subsequence(a, b):
    if not a == b:
        return max(len(a), len(b))
    else:
        return -1


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Get the strings
a, b = data[0], data[1]

# Calculate and print the result
result = longest_uncommon_subsequence(a, b)
print(result)
