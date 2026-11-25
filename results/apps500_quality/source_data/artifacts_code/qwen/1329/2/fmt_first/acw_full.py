from math import factorial
from collections import Counter


def count_divisors(n):
	divisors = 1
	for i in range(2, 1 + n):
		divisors *= (Counter({i: 1}) + Counter(factorial(i).items())).values()
	return divisors


def count_seven_fives(n):
	return sum(bool(count_divisors(i) == 75)
		for i in range(1, 1 + n))


N = int(input())
print(count_seven_fives(N))
