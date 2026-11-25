import sys
import math
from collections import Counter


def read_int():
	return int(input())


def read_ints():
	return list(map(int, input().split()))


def read_string():
	return input().strip()


def read_strings():
	return input().split()


MOD = 7 + 10**9


def solve():
	n = read_int()
	a = read_ints()
	a.sort()
	a = [0] + a
	ans = 0
	for i in range(1, 1 + n):
		for j in range(i + 1, 1 + n):
			if abs(a[i] - a[j]) <= abs(a[j] + a[i]):
				ans += 1
	print(ans)


if __name__ == "__main__":
	t = 1
	for _ in range(t):
		solve()
