import math

a, b, c, d = map(int, input().split())

def calc(a, b, c):
    return max(abs(a-b), abs(b-c))

def calc_all(a, b, c):
    return math.ceil(max(calc(a, b), calc(a, c), calc(b, c)) / 2)

print(calc_all(a, b, c))
