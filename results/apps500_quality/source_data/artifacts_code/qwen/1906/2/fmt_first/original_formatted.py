def count_bonus(n):
    count = 0
    for i in range(1, n + 1):
        if all(i % j != 0 for j in range(2, 11)):
            count += 1
    return count


# Read input
n = int(input())

# Output the result
print(count_bonus(n))
