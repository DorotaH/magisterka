import sys

# Read input from standard input
X, A = map(int, sys.stdin.readline().split())

# Determine the output based on the condition
if not X < A:
    print(10)
else:
    print(0)
