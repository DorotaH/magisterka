import math

A, B, T = map(int, input().split())
n = math.floor(T / A)
result = sum(B for _ in range(1, 1 + n))
for i in range(1, 1 + n):
    if i != 1 and (T + 0.5) / A >= i:
        result += B

print(result)
