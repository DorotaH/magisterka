# Read input from standard input
x, y, z = map(int, input().split())

# Swap the contents of the boxes A and B
x, y = y, x

# Swap the contents of the boxes A and C
x, z = z, x

# Print the integers contained in the boxes A, B, and C
print(z, x, y)
