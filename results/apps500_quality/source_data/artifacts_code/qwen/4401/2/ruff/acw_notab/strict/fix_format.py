# Read input from standard input
X, Y, Z = map(int, input().split())

# Swap the contents of boxes A and B
X, Y = Y, X

# Swap the contents of boxes A and C
X, Z = Z, X

# Print the contents of boxes A, B, and C
print(X, Y, Z)
