import math


def is_prime(n):
	"""Check if a number is prime."""
	if n <= 1:
		return False
	return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


t = int(input())  # Number of test cases

for _ in range(t):
	x, y = map(int, input().split())  # Read two integers
	diff = x - y  # Calculate the difference between x and y

	# Find the largest prime number that is less than or equal to the difference
	p = max(i for i in range(2, diff + 1) if is_prime(i))

	# If the difference is divisible by the prime, it's possible to reach y
	if diff % p == 0:
		print("YES")
	else:
		print("NO")
