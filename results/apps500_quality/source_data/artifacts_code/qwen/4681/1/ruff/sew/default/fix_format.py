import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Initialize the first two Lucas numbers
l0 = 2
l1 = 1

# Compute the N-th Lucas number
for _ in range(N):
    l0, l1 = l1, l0 + l1

# Print the N-th Lucas number
print(l0)
