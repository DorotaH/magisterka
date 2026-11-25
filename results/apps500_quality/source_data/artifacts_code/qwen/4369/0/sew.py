import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the number of sheets needed
sheets_needed = (1 + N) // 2

# Print the result
print(sheets_needed)