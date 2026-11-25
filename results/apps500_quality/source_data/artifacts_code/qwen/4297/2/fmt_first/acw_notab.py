import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Find the minimum positive integer divisible by both 2 and N
result = N if N % 2 == 0 else 2 * N
# Print the result to standard output
print(result)
