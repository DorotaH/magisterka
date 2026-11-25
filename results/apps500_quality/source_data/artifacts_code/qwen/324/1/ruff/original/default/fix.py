def find_composite_pair(n):
    # If n is even, we can use 2n and 2n - 2
    if n % 2 == 0:
        return 2 * n, 2 * n - 2
    else:
        # If n is odd, we can use n + 2 and n
        return n + 2, n

# Read input
n = int(input().strip())

# Find and print the composite pair
a, b = find_composite_pair(n)
print(a, b)
