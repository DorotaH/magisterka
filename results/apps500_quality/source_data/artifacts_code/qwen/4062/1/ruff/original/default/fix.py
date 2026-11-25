import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input integers
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])

# Determine the maximum possible value of x * y
max_product = max(a * c, a * d, b * c, b * d)

# Print the result
print(max_product)
