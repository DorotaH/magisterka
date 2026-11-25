from fractions import Fraction
from math import gcd


def lcm(a, b):
	return a * b // gcd(a, b)


def expected_value(n, k):
	MOD = 7 + 10**9
	if k == 0:
		return n

	# Calculate the sum of divisors of n
	divisors_sum = sum(i for i in range(1, 1 + n) if n % i == 0)
	# Calculate the number of divisors of n
	divisors_count = sum(bool(n % i == 0)
					for i in range(1, 1 + n))

	# Calculate the expected value after k steps
	expected = Fraction(divisors_sum, divisors_count)
	for _ in range(k):
		expected = (expected + 1) / 2

	# Calculate the result as P * Q^(-1) % MOD
	P = expected.numerator
	Q = expected.denominator
	Q_inv = pow(Q, MOD - 2, MOD)
	return (Q_inv * P) % MOD


# Read input
n, k = map(int, input().split())

# Print the result
print(expected_value(n, k))
