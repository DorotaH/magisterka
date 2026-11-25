import math


def find_composite(a, n):
	"""Find the next composite number after a."""
	for i in range(a + 1, 10 ** 9):
		if not is_prime(i):
			return i


def is_prime(n):
	"""Check if a number is prime."""
	if n <= 1:
		return False
	return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


def solve(n):
	"""Find two composite integers a and b such that a - b = n."""
	a = 2
	while True:
		a = find_composite(a, n)
		if is_prime(a - n):
			b = a - n
			return f"{a} {b}"


n = int(input())
print(solve(n))
