import sys

# Read input from standard input
input = sys.stdin.read().strip()

# Split the input into two strings S and T
S, T = input.split()

# Concatenate T and S in this order
result = T + S

# Print the resulting string
print(result)
