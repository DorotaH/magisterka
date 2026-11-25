# Read input from standard input
A, B = map(int, input().split())

# Calculate the three possible results
sum_result = A + B
diff_result, prod_result = A - B, A * B

# Determine and print the largest result
print(max(sum_result, diff_result, prod_result))