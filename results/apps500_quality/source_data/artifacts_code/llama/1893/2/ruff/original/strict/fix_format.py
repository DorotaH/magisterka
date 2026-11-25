import math

n, t = map(int, input().split())

result = n * 1.000000011**t

print(math.floor(result * 1e6) / 1e6)
