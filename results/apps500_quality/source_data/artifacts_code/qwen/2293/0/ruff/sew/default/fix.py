from functools import reduce
from math import gcd


def lcm(a, b):
    return  b * a // gcd(a, b)

def lcm_multiple(numbers):
    return  reduce(lcm, numbers)

def can_dora_win(m, n, days):
    for  day in  days:
        dora_stores = set(day[1:])
        if  len(dora_stores) != len(day[1:]):
            return  "impossible"
        dora_lcm, swiper_lcm = lcm_multiple([i for i in range(1, n+1) if i in dora_stores]), lcm_multiple([i for i in range(1, n+1) if i not in dora_stores])
        if  swiper_lcm >= dora_lcm:
            return  "impossible"
    return  "possible"

# Read input
m, n=map(int, input().split())
days = [tuple(map(int, input().split())) for _ in range(m)]

# Output result
print(can_dora_win(m, n, days))