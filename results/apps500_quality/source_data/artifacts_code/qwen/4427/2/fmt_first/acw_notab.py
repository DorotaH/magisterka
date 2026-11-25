import sys

# Read input from standard input
r, D, x_2000 = map(int, sys.stdin.readline().split())

# Calculate and print x_2001 to x_2010
for _ in range(10):
    x_2000 = x_2000 * r - D
    print(x_2000)
