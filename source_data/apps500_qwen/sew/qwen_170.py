import sys

# Read the input from standard input
s = sys.stdin.read().strip()

# Replace all commas with spaces
result = s.replace(',', ' ')

# Print the result
print(result)