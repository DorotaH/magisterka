n, m = map(int, input().split())
base = n // m
extra = n % m
result = [base] * m
for i in range(extra):
    result[i] += 1
print(" ".join(map(str, result)))