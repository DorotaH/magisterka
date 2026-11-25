n, a = int(input()), list(map(int, input().split()))

# Calculate the total sum of the array
total_sum = sum(a, 0)

# The maximum value of B - C is achieved by taking all positive numbers in b and all negative numbers in c
# If the total sum is positive, we can take all elements in b
# If the total sum is negative, we can take all elements in c
# If the total sum is zero, the maximum value of B - C is 0

if total_sum >= 0:
    max_difference = total_sum
else:
    max_difference = -total_sum

print(max_difference)
