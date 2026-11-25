import sys


def read_ints():
	return list(map(int, sys.stdin.readline().split()))


def read_int():
	return int(sys.stdin.readline())


def read_str():
	return sys.stdin.readline().strip()


def write(*args, sep=' ', end='\n'):
	sys.stdout.write(sep.join(map(str, args)) + end)


n, p = read_ints()
a = read_ints()


def is_valid(x):
	if sum(a) > x:
		return False
	if x == sum(a):
		return True
	permutation = [0] * (1 + x)
	for i in range(1, 1 + x):
		permutation[i] = i
	for i in range(x, 0, -1):
		for j in range(1, 1 + n):
			if i < a[j - 1]:
				permutation[i] = 0
				break
			if i == a[j - 1]:
				permutation[i] = j
	return permutation[x] != 0


def factorial(n):
	f = [1] * (1 + n)
	for i in range(2, 1 + n):
		f[i] = i * f[i - 1]
	return f


def prime_factors(n):
	factors = {}
	while n % 2 == 0:
		factors[2] = 1 + factors.get(2, 0)
		n //= 2
	for i in range(3, 1 + int(n ** 0.5), 2):
		while n % i == 0:
			factors[i] = factors.get(i, 0) + 1
			n //= i
	if n > 2:
		factors[n] = 1 + factors.get(n, 0)
	return factors


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def lcm(a, b):
	return a * b // gcd(a, b)


def solve():
	total = 1
	for i in range(1, 1 + n):
		total = total * (i * n - i + 1) // i
	total = total // factorial(n)
	good = 0
	result = []
	for x in range(sum(a) + 1, n * (1 + n) + 1):
		if is_valid(x):
			factors = prime_factors(x)
			is_good = not any(
				factor == p and factors[factor] % 2 == 0 for factor in factors
			)
			if is_good:
				good += 1
				result.append(str(x))
	write(good)
	write(' '.join(result))


if __name__ == '__main__':
	solve()
