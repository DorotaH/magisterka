from fractions import Fraction


def gcd(x, y):
	while y:
		x, y = y, x % y
	return x


def can_equalize(a, b):
	return gcd(a, b) == 1


def min_minutes(a1, b1, a2, b2):
	if can_equalize(a1, b1) and can_equalize(a2, b2):
		return -1
	if can_equalize(a1, b1):
		return 1, a1, b1, a2, b2
	if can_equalize(a2, b2):
		return 1, a2, b2, a1, b1
	if a1 % 2 == 0 and b1 % 2 == 0:
		return 2, a1 // 2, b1 // 2, a2, b2
	if a2 % 2 == 0 and b2 % 2 == 0:
		return 2, a2 // 2, b2 // 2, a1, b1
	if a1 % 3 == 0 and b1 % 3 == 0:
		return 2, a1 // 3, b1 // 3, a2, b2
	return (2, a2 // 3, b2 // 3, a1, b1) if a2 % 3 == 0 and b2 % 3 == 0 else -1


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

result = min_minutes(a1, b1, a2, b2)
if result == -1:
	print(result)
else:
	print(result[0])
	print(result[1], result[2])
	print(result[3], result[4])
