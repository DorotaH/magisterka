# Read input values
A, B, C = map(int, input().split())

# Calculate the maximum possible allowance
max_allowance = max(A * 10 + B + C, A + B * 10 + C, A + B + C * 10)

# Print the result
print(max_allowance)
