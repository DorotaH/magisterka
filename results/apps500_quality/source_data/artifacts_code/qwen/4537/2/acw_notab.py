import sys

# Read input from standard input
A, B = map(int, sys.stdin.read().split())

# Calculate the three values
sum_AB = B + A
diff_AB = A - B
prod_AB = B * A

# Find the maximum value
max_value = max(sum_AB, diff_AB, prod_AB)

# Print the maximum value
print(max_value)
