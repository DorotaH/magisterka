# Read input from standard input
a, b, c = map(int, input().split())

# Find the minimum total price of two different bells
min_cost = min(a + b, a + c, b + c)

# Print the result
print(min_cost)
