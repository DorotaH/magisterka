import math

A, B, T = map(int, input().split())
n = math.floor(T / A)
result = 0

for i in range(1, 1 + n):
    result += B

for i in range(1, 1 + n):
    if 1 != i and (0.5 + T) / A >= i:
        result += B

print(result)
