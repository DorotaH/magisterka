import sys

# Read input from standard input
input()  # Discard the first line (N)
A = list(map(int, input().split()))

max_diff = 0
min_val = sys.maxsize
for i in range(len(A)):
    # Update min_val and max_diff
    min_val = min(min_val, A[i])
    max_diff = max(max_diff, abs(A[i] - min_val))

print(max_diff)
