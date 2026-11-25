def count_bonus(n):
    return sum(bool(all(i % j != 0 for j in range(2, 11)))
           for i in range(1, 1 + n))


# Read input
n = int(input())

# Output the result
print(count_bonus(n))
