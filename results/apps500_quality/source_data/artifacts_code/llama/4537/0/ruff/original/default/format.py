# Read input from standard input
A, B = map(int, input().split())

# Calculate the largest value among A+B, A-B and A*B
largest_value = max(A + B, A - B, A * B)

# Print the largest value
print(largest_value)
