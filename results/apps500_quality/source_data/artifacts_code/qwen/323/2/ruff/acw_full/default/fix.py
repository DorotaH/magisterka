import math


def gcd_of_factorials(a, b):
	if a > b:
		a, b = b, a
	return math.gcd(math.factorial(a), math.factorial(b))


# Read input
a, b = map(int, input().split())

# Output the result
print(gcd_of_factorials(a, b))
