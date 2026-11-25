# Read the input from standard input
A, B = map(int, input().split())

# Calculate the area of the yard excluding the roads
area = B * A - 2 * (B + A - 2) + 1

# Print the result
print(area)
