from  math import  gcd
from  functools import  reduce

def lcm(a, b):
    return a * b//gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def is_possible(m, n, days):
    for  day in  days:
        s_i, stores_dora = day[0], day[1]
        stores_swiper = [i for i in range(1, n + 1) if i not in stores_dora]
        lcm_dora, lcm_swiper = lcm_multiple([i for i in range(1, n + 1) if i in stores_dora]), lcm_multiple([i for i in range(1, n + 1) if i in stores_swiper])
        if lcm_swiper >= lcm_dora:
            return  "impossible"
    return "possible"

# Read input
m, n=map(int, input().split())
days = []
for _ in range(m):
    days.append(tuple(map(int, input().split())))

# Output the result
print(is_possible(m, n, days))
