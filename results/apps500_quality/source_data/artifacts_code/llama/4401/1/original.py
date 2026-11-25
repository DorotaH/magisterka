# Read input from standard input
X, Y, Z = map(int, input().split())

# Swap the contents of the boxes A and B
temp = X
X = Y
Y = temp

# Swap the contents of the boxes A and C
temp = X
X = Z
Z = temp

# Print the contents of the boxes A, B, and C
print(X, Y, Z)
