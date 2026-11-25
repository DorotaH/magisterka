from functools import reduce
from math import gcd
from sys import stdin


def lcm(a, b):
	return a * b // gcd(a, b)


def solve():
	N = int(stdin.readline())
	T = []
	A = []
	for _ in range(N):
		T_i, A_i = map(int, stdin.readline().split())
		T.append(T_i)
		A.append(A_i)

	def lcm_list(L):
		return reduce(lcm, L)

	def solve():
		min_val = 1
		for i in range(1, N + 1):
			min_val = lcm(min_val, T[i - 1] * A[i - 1])
		return min_val

	print(solve())


if __name__ == "__main__":
	solve()
