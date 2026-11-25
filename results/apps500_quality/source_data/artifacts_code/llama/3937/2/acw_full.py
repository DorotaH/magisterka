import math
import sys
import functools


def main():
	input = sys.stdin.readline
	n, m, k = map(int, input().split())
	a = list(map(int, input().split()))

	def gcd(a, b):
		while b:
			a, b = b, a % b
		return a

	def get_row(i):
		return [gcd(i, j) for j in range(1, 1 + m)]

	rows = [get_row(i) for i in range(1, 1 + n)]

	for row in rows:
		for i in range(len(row) - k + 1):
			if all(x == y for x, y in zip(row[i:i + k], a)):
				return 'YES'

	return 'NO'


print(main())
