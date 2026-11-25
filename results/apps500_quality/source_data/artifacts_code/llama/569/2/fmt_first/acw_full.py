from collections import defaultdict
from sys import stdin


def read_int():
	return int(stdin.readline())


def read_ints():
	return map(int, stdin.readline().split())


def read_str():
	return stdin.readline().strip()


def read_strs():
	return stdin.readline().split()


def solve():
	n = read_int()
	s = read_str()

	d = defaultdict(int)
	for i in range(n):
		for j in range(i + 1, 1 + n):
			d[tuple(s[i:j])] += 1
			if d[tuple(s[i:j])] > 1:
				return -1

	ans = 0
	for i in range(n):
		for j in range(i + 1, n):
			if s[i] == s[j]:
				ans += 1
				s = s[:i] + chr(ord(s[i]) + 1) + s[i + 1 : j] + s[1 + j :]
	return ans


print(solve())
