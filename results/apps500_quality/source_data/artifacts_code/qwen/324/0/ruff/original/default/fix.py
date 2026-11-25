import sys


def find_composite_pair(n):
    # If n is even, we can use 2n and 2n - n = n
    if n % 2 == 0:
        return 2 * n, n
    else:
        # If n is odd, we can use 4n and 4n - n = 3n
        return 4 * n, 3 * n

# Read input
n = int(sys.stdin.read().strip())

# Find and print the composite pair
a, b = find_composite_pair(n)
print(a, b)
