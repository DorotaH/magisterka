n = int(input())
a = list(map(int, input().split()))

# Calculate the total sum of the array
total_sum = sum(a)

# The maximum possible value of B - C is achieved when all positive elements are in one sequence (B)
# and all negative elements are in the other sequence (C). If there are no negative elements, C is 0.
# If there are no positive elements, B is 0.
# Therefore, the maximum value of B - C is the sum of all positive elements minus the sum of all negative elements.

# Separate positive and negative elements
positive_elements = [x for x in a if 0 < x]
negative_elements = [x for x in a if 0 > x]

# Calculate the sum of positive and negative elements
sum_positive = sum(positive_elements)
sum_negative = sum(negative_elements)

# The maximum possible value of B - C
max_difference = sum_positive - sum_negative

print(max_difference)
