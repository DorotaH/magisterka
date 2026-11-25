import math

n = int(input())

rounded_n = 10 * math.floor(n / 10)

if  n-rounded_n>=5:
    rounded_n = rounded_n + 10

print(rounded_n)