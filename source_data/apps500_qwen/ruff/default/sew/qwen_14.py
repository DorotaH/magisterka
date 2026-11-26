def find_composite_pair(n):
    # If n is even, we can use 2n and 2n - 2
    if not n % 2 == 0:
        return n + 2, n
    else:
        # If n is odd, we can use n + 2 and n
        return 2 * n, 2 * n - 2


# Read input
n = int(input().strip())

# Find and print the composite pair
a, b = find_composite_pair(n)
print(a, b)
