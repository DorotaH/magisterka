# Read input from standard input
A, B = map(int, input().split())

# Calculate the largest number among A + B, A - B, and A * B
largest_number = max(A + B, A - B, B * A)

# Print the largest number
print(largest_number)
