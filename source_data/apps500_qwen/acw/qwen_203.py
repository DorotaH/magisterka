import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the integers X, Y, and Z
X, Y, Z = map(int, data)

# Perform the swaps
A, B = Y, X
A, C = Z, A

# Print the final contents of the boxes
print(A, B, C)
