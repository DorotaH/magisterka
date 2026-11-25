import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Find the minimum positive integer divisible by both 2 and N
if N % 2 == 0:
    result = N
else:
    result = N * 2

# Print the result to standard output
print(result)