
a, b = map(int, input().split())


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


g = gcd(a, b)

a //= g
b //= g


def min_resistors(a, b):
	if a == 1:
		return b
	if a < b:
		a, b = b, a
	a %= b
	if a == 0:
		return b
	return a + 1 if b == 1 else 2 * min_resistors(b, a % b) + 1


print(min_resistors(a, b))
