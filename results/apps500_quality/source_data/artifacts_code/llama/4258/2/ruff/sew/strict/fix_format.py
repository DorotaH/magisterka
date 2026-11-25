import math

A, B, T = map(int, input().split())
n = math.floor(T / A)
result = 0

for i in range(1, 1 + n):
    result += B

for i in range(1, 1 + n):
    if i != 1 and i <= (0.5 + T) / A:
        result += B

print(result)
