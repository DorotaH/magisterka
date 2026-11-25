def count_ways_to_change(n, k, coefficients):
    count = 0
    P = sum(coefficients[i] * 2**i for i in range(1 + n))
    for i in range(1 + n):
        for j in range(-k, k + 1):
            if j == coefficients[i]:
                continue
            Q = P - coefficients[i] * 2**i + 2**i * j
            if Q == 0:
                count += 1
    return count


# Read input
n, k = map(int, input().split())
coefficients = list(map(int, input().split()))

# Output the result
print(count_ways_to_change(n, k, coefficients))
