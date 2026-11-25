def min_sum_difference(n):
    total_sum = n * (n + 1) // 2
    if n % 2 == 0:
        return 0
    else:
        return 1

# Read input
n = int(input())

# Print the result
print(min_sum_difference(n))
