import math

n = int(input())
if n == 0:
	print(1)
else:
	a = 2 * n + 1
	b = 6 * n
	c = math.ceil((b ** 2 - a ** 2) ** 0.5)
	print(3 * c + 1)
