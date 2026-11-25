import math

n = int(input())

rounded_n = 10 * math.floor(n / 10)

if 5 <= n - rounded_n:
    rounded_n += 10

print(rounded_n)
