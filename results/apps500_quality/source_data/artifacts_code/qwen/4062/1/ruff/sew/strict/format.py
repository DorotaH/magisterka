import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input integers
a, b = int(data[0]), int(data[1])
c, d = int(data[2]), int(data[3])

# Determine the maximum possible value of x * y
max_product = max(c * a, d * a, c * b, d * b)

# Print the result
print(max_product)
