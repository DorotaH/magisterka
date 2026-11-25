# Read input from standard input
k, a, b = map(int, input().split())

# Calculate the number of k-divisible numbers
count = (b // k) - (-(-a // k)) + 1

# Print the result
print(count)
