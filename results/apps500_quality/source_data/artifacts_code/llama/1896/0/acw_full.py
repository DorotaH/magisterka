import math

n = int(input())

if n == 0:
	print(1)
else:
	print(6 * (2 * n**2 + 3 * n + 1) - 3 * n - 1)
