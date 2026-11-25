import sys

# Read input from standard input
a, b, c = map(int, sys.stdin.readline().split())

# Calculate the minimum total price of two different bells
min_price = min(a + b, a + c, b + c)

# Print the minimum total price
print(min_price)