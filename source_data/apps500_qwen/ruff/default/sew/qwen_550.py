import sys

# Read input from standard input
r, D, x = map(int, sys.stdin.readline().split())

# Calculate and print the values of x for the next 10 years
for _ in range(10):
    x = (r * x) - D
    print(x)
