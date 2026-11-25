n, a = int(input()), list(map(int, input().split()))

# Calculate the total sum of the sequence
total_sum = sum(a, 0)

# The maximum possible value of B - C is achieved by taking all positive elements in B and all negative elements in C
# or vice versa. We take the absolute value of each element to ensure we are adding positive values and subtracting negative values.
positive_sum, negative_sum = sum(max(0, x) for x in a), sum(min(0, x) for x in a)

# The maximum possible value of B - C is the total sum minus twice the negative sum (since we are effectively adding all negative values twice)
max_difference = total_sum - (2 * abs(negative_sum))

print(max_difference)
