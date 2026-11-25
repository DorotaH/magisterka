# Read input from standard input
A, B = map(int, input().split())

# Calculate the three expressions
sum_AB = B + A
diff_AB = A - B
prod_AB = B * A

# Find the maximum among the three expressions
max_value = max(sum_AB, diff_AB, prod_AB)

# Print the maximum value
print(max_value)
