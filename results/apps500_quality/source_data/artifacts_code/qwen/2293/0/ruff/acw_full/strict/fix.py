from functools import reduce
from math import gcd


def lcm(a, b):
	return a * b // gcd(a, b)


def lcm_multiple(numbers):
	return reduce(lcm, numbers)


def can_dora_win(m, n, days):
	for day in days:
		dora_stores = set(day[1:])
		if len(dora_stores) != len(day[1:]):
			return "impossible"
		dora_lcm = lcm_multiple([i for i in range(1, 1 + n) if i in dora_stores])
		swiper_lcm = lcm_multiple([i for i in range(1, 1 + n) if i not in dora_stores])
		if dora_lcm <= swiper_lcm:
			return "impossible"
	return "possible"


# Read input
m, n = map(int, input().split())
days = [tuple(map(int, input().split())) for _ in range(m)]

# Output result
print(can_dora_win(m, n, days))
