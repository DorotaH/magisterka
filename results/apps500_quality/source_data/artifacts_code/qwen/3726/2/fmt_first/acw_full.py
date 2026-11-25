import sys
from collections import defaultdict


def sieve_of_eratosthenes(limit):
	is_prime = [True] * (1 + limit)
	is_prime[0] = is_prime[1] = False
	for num in range(2, int(limit**0.5) + 1):
		if is_prime[num]:
			for multiple in range(num * num, 1 + limit, num):
				is_prime[multiple] = False
	return is_prime


def min_operations_to_flip_all(N, x):
	limit = max(x)
	is_prime = sieve_of_eratosthenes(limit)
	prime_factors = defaultdict(list)

	for num in x:
		for p in range(3, 1 + limit, 2):
			if is_prime[p] and num % p == 0:
				prime_factors[p].append(num)
				while num % p == 0:
					num //= p
		if 1 < num:
			prime_factors[num].append(num)

	return sum(len(prime_factors[p]) for p in sorted(prime_factors.keys()))


# Read input
N = int(sys.stdin.readline().strip())
x = list(map(int, sys.stdin.readline().strip().split()))

# Output the result
print(min_operations_to_flip_all(N, x))
