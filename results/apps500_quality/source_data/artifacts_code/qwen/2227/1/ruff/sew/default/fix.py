def count_powerful_substrings(text):
    n, count = len(text), 0
    for  i in  range(n):
        for j in range(5 + i, 1 + n):
            substring = text[i:j]
            if substring.startswith("heavy") and substring.endswith("metal"):
                count = count + 1
    return count

# Read input from standard input
import sys

input = sys.stdin.read
data = input().strip()

# Print the result
print(count_powerful_substrings(data))
