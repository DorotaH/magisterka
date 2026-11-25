import math

T = int(input())

for _ in range(T):
	n = int(input())
	print((n % 2) + math.ceil(n / 2))
