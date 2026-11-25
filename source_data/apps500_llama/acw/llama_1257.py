import sys


def gcd(a, b):
	"""Calculate the greatest common divisor of two integers."""
	while b:
		a, b = b, a % b
	return a


def main():
	"""Read the input and print the number of xorangles."""
	n = int(input())
	count = 0
	for a in range(1, n):
		for b in range(a, n):
			for c in range(b, n):
				if a + b > c and b + c > a and a + c > b and a + b + c <= 2 * n and gcd(a, b + c) == 1:
					count += 1
	print(count)


if __name__ == "__main__":
	main()
