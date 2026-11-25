def min_sum_difference(n):
    total_sum = n * (1 + n) // 2
    return 0 if n % 2 == 0 else 1


# Read input
n = int(input())

# Print the result
print(min_sum_difference(n))
