def count_bonus(n):
    def is_not_divisible_by_any(i):
        for j in range(2, 11):
            if i % j == 0:
                return False
        return True

    count = 0
    for i in range(1, n + 1):
        if is_not_divisible_by_any(i):
            count += 1
    return count

# Read input from standard input
n = int(input().strip())

# Print the result
print(count_bonus(n))
