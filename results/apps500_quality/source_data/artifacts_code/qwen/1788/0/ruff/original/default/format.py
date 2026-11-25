# Read input from standard input
A, B = map(int, input().split())

# Calculate X and Y
X = (A + B) // 2
Y = (A - B) // 2

# Print the result
print(X, Y)
