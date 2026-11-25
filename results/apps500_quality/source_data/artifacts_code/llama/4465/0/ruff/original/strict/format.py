# Read the input from standard input
A, B = map(int, input().split())

# Calculate the area of the yard excluding the roads
area = A * B - 2 * (A + B - 2) + 1

# Print the result
print(area)
