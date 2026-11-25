import sys


def gcd(a, b):
	"""Compute the greatest common divisor of a and b"""
	while b:
		a, b = b, a % b
	return a


def lcm(a, b):
	"""Compute the lowest common multiple of a and b"""
	return a * b // gcd(a, b)


n = int(sys.stdin.readline())
print((n - 2) * (n - 1) // 2)
