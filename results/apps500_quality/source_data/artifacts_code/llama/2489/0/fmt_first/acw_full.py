import math
import sys


def gcd(a, b):
	"""Compute the greatest common divisor of a and b"""
	while b:
		a, b = b, a % b
	return a


n = int(input())
A = [int(x) for x in input().split()]

max_a = max(A)
factors = [[] for _ in range(1 + max_a)]

for i in range(1, 1 + int(math.sqrt(max_a))):
	if i * i <= max_a:
		factors[i].append(i)
		factors[i * i].append(i)
	if i <= max_a // i:
		factors[i].append((max_a // i) * i)

for i in range(1, 1 + max_a):
	if len(factors[i]) == 0:
		factors[i].append(i)

for i in range(n):
	for factor in factors[A[i]]:
		if factor != A[i]:
			A[i] = False
			break

count = sum(bool(A[i])
		for i in range(n))
print(count)
