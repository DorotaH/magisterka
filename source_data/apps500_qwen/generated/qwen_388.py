def max_pushes(n):
    return n * (n + 1) // 2

# Read input
n = int(input().strip())

# Calculate and print the result
print(max_pushes(n))
