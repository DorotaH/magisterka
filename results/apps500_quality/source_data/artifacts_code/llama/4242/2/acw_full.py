import math


def gcd(a, b):
	"""Compute the greatest common divisor of a and b"""
	while b:
		a, b = b, a % b
	return a


def kth_largest_divisor(A, B, K):
	"""Find the K-th largest positive integer that divides both A and B"""
	# Compute the greatest common divisor of A and B
	gcd_ab = gcd(A, B)
	
	# Find all divisors of gcd_ab
	divisors = [i for i in range(1, 1 + gcd_ab) if gcd_ab % i == 0]
	
	# Sort the divisors in descending order
	divisors.sort(reverse=True)
	
	# Return the K-th largest divisor
	return divisors[K - 1]


A, B, K = map(int, input().split())
print(kth_largest_divisor(A, B, K))
