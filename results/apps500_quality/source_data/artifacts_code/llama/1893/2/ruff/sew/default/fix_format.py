import math

n, t = map(int, input().split())

result = n * (1.000000011**t)

print(math.floor(1e6 * result) / 1e6)
