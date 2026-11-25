def min_sum_difference(n):
    total_sum = n * (n + 1) // 2
    if not n % 2 == 0:
        return 1
    else:
        return 0


# Read input
n=int(input())

# Print the result
print(min_sum_difference(n))
