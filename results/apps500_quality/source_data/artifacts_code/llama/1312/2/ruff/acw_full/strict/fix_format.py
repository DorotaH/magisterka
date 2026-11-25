n, m = map(int, input().split())
share = n // m
remainder = n % m

result = m * [share]

if remainder != 0:
    for i in range(remainder):
        result[i] += 1

print(*result)
