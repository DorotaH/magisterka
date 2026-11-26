# Read input from standard input
A, B = map(int, input().split())

# Calculate the three expressions
sum_AB = A + B
diff_AB, prod_AB = A - B, A * B

# Find the maximum among the three expressions
max_value = max(sum_AB, diff_AB, prod_AB)

# Print the maximum value
print(max_value)
