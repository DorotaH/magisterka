def count_powerful_substrings(text):
    n = len(text)
    count = 0
    for i in range(n):
        for j in range(i + 5, n + 1):
            substring = text[i:j]
            if substring.startswith("heavy") and substring.endswith("metal"):
                count += 1
    return count

# Read input from standard input
import sys
input = sys.stdin.read
data = input().strip()

# Print the result
print(count_powerful_substrings(data))
