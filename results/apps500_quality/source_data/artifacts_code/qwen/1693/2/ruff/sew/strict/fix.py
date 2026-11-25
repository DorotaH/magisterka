def max_skyscrapers(n, m):
    # Initialize the result array with the minimum possible values
    a=[1]*n

    # Iterate from the second plot to the last plot
    for i in range(1, n):
        # The number of floors for the current plot is the minimum of the current plot's limit and the previous plot's value plus one
        a[i] = min(m[i], 1 + a[i-1])

    # Return the result array
    return a

# Read input
n = int(input())
m = list(map(int, input().split()))

# Calculate the result
result = max_skyscrapers(n, m)

# Print the result
print(' '.join(map(str, result)))
