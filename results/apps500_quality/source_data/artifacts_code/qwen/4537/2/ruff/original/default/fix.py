import sys

# Read input from standard input
A, B = map(int, sys.stdin.read().split())

# Calculate the three values
sum_AB = A + B
diff_AB = A - B
prod_AB = A * B

# Find the maximum value
max_value = max(sum_AB, diff_AB, prod_AB)

# Print the maximum value
print(max_value)
