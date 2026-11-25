import sys

# Read input from standard input
r, D, x_2000 = map(int, sys.stdin.readline().split())

# Calculate and print x_2001 to x_2010
for i in range(10):
    x_2000 = r * x_2000 - D
    print(x_2000)
