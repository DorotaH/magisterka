# Read input from standard input
A, B = map(int, input().split())

# Calculate the three possible values
sum_result = A + B
diff_result, prod_result = A - B, A * B

# Find the largest value among the three
largest_value = max(sum_result, diff_result, prod_result)

# Print the largest value
print(largest_value)
