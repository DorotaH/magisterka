import math

n, t = map(int, input().split())

result = 1.000000011 ** t * n

print(math.floor(result * 1e6) / 1e6)
