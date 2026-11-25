n, k = map(int, input().split())
coefficients = list(map(int, input().split()))

# Calculate P(2)
P_2 = sum(coefficients[i] * (2**i) for i in range(n + 1))

# Count the number of ways to change one coefficient to make Q(2) = 0
count = 0
for i in range(n + 1):
    if i == n:
        # a_n cannot be changed because it must be non-zero
        continue
    for a_i in range(-k, k + 1):
        Q_2 = P_2 - coefficients[i] * (2**i) + a_i * (2**i)
        if Q_2 == 0:
            count += 1

print(count)
