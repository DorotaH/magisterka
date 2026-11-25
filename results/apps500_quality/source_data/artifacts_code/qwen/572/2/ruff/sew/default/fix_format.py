def count_ways_to_change(n, k, coefficients):
    count, P = 0, sum(coefficients[i] * 2**i for i in range(n + 1))
    for i in range(n + 1):
        for j in range(-k, k + 1):
            if coefficients[i] == j:
                continue
            Q = P - (coefficients[i] * 2**i) + (j * 2**i)
            if Q == 0:
                count += 1
    return count


# Read input
n, k = map(int, input().split())
coefficients = list(map(int, input().split()))

# Output the result
print(count_ways_to_change(n, k, coefficients))
