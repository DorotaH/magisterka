import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Initialize the first two Lucas numbers
L0, L1 = 2, 1

# If N is 0, the result is L0
if N == 0:
    result = L0
# If N is 1, the result is L1
elif N == 1:
    result = L1
else:
    # Compute the N-th Lucas number using the recurrence relation
    for _ in range(2, N + 1):
        L0, L1 = L1, L1 + L0
    result = L1

# Print the result
print(result)
