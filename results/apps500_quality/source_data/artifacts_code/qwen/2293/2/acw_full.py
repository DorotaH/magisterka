from math import gcd
from functools import reduce


def lcm(a, b):
	return a * b // gcd(a, b)


def lcm_multiple(numbers):
	return reduce(lcm, numbers)


def is_possible(m, n, days):
	for day in days:
		s_i = day[0]
		stores_dora = day[1]
		stores_swiper = [i for i in range(1, 1 + n) if i not in stores_dora]
		lcm_dora = lcm_multiple([i for i in range(1, 1 + n) if i in stores_dora])
		lcm_swiper = lcm_multiple([i for i in range(1, 1 + n) if i in stores_swiper])
		if lcm_swiper >= lcm_dora:
			return "impossible"
	return "possible"


# Read input
m, n = map(int, input().split())
days = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(is_possible(m, n, days))
