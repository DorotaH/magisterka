import math

r = int(input())


def solve():
	for x in range(1, int(math.sqrt(r)) + 1):
		y = (r - x**2 - x - 1) / (2 * x)
		if y.is_integer() and y > 0:
			return f"{x} {int(y)}"
	return "NO"


print(solve())
