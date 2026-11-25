import math

A, B, T = map(int, input().split())
n = math.floor(T / A)
result = 0

for i in range(1, n + 1):
    result += B

for i in range(1, n + 1):
    if i != 1 and i <= (T + 0.5) / A:
        result += B

print(result)
