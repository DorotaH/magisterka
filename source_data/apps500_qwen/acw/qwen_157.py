import sys

# Read input from standard input
A, B = map(int, sys.stdin.read().split())

# Calculate the three expressions
sum_result = B + A
difference_result = A - B
product_result = B * A

# Find the largest number among the three
largest_number = max(sum_result, difference_result, product_result)

# Print the largest number
print(largest_number)
