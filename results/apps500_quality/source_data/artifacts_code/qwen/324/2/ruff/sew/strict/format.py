import sys


def find_composite_pair(n):
    # Function to check if a number is composite
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False

    # Start checking from n+2 upwards to find a composite number
    for a in range(2 + n, 10**9):
        if is_composite(a):
            b = a - n
            if is_composite(b):
                return a, b


# Read input
n = int(sys.stdin.read().strip())

# Find and print the composite pair
a, b = find_composite_pair(n)
print(a, b)
