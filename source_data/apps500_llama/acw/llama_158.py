# Read input from standard input
A, B = map(int, input().split())

# Calculate the three possible results
sum_result = B + A
diff_result = A - B
prod_result = B * A

# Determine and print the largest result
print(max(sum_result, diff_result, prod_result))
