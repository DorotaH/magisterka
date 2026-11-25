# Read input from standard input
A, B = map(int, input().split())

# Calculate the three possible values
sum_result = B + A
diff_result = A - B
prod_result = B * A

# Find the largest value among the three
largest_value = max(sum_result, diff_result, prod_result)

# Print the largest value
print(largest_value)
