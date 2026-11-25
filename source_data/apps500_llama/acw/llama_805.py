import sys
import math


def solve():
	p, q = map(int, sys.stdin.readline().split())
	a = list(map(int, sys.stdin.readline().split()))
	b = list(map(int, sys.stdin.readline().split()))
	d = list(map(int, sys.stdin.readline().split()))
	X = list(map(int, sys.stdin.readline().split()))

	n = len(X)
	m = 10**6

	for i in range(1, 1 + p):
		a[i] %= m
	for i in range(1, q + 1):
		d[i] %= m

	def find_coefficients(a, b, p, q):
		A = []
		for i in range(1, 1 + p):
			A.append(a[i])

		for i in range(1, q + 1):
			A.append(b[i])

		return A

	A = find_coefficients(a, b, p, q)
	B = [0] * (1 + n)

	for i in range(n):
		B[i + 1] = (sum(A[j] * X[i - j + 1] for j in range(min(i + 1, 1 + p))) + sum(d[k] * pow(10, k, m) for k in range(min(i + 1, q + 1))) % m) % m

	for i in range(10):
		print(B[i + n], end=' ')


def main():
	T = 1
	for _ in range(T):
		solve()


if __name__ == '__main__':
	main()
