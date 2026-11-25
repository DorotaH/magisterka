import math


def count_shichi_go(N):
	def prime_factors(n):
		i = 2
		factors = []
		while i**2 <= n:
			if n % i:
				i += 1
			else:
				n //= i
				factors.append(i)
		if 1 < n:
			factors.append(n)
		return factors

	def count_divisors(factors):
		from collections import Counter
		counter = Counter(factors)
		count = 1
		for v in counter.values():
			count *= (1 + v)
		return count

	def num_factors(n):
		factors = prime_factors(n)
		return count_divisors(factors)

	def num_shichi_go(N):
		count = 0
		for i in range(1, N + 1):
			if num_factors(math.factorial(i)) == 75:
				count += 1
		return count

	return num_shichi_go(N)


N = int(input())
print(count_shichi_go(N))
