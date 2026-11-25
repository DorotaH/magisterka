import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the minimum number of sheets needed
sheets_needed = (N + 1) // 2

# Print the result
print(sheets_needed)
