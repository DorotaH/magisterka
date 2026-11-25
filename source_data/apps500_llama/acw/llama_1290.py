from collections import Counter
from itertools import accumulate
import sys
input = sys.stdin.readline


def read_int():
	return int(input())


def read_ints():
	return map(int, input().split())


def read_ints_minus_one():
	return map(lambda x: int(x) - 1, input().split())


def read_str():
	return input().strip()


def read_strs():
	return map(lambda x: x.strip(), input().split())


def solve():
	k, n = read_ints()
	s = [read_str() for _ in range(k)]
	c = [Counter() for _ in range(k)]
	for i in range(n):
		for j in range(k):
			c[j][s[j][i]] += 1
	for i in range(n):
		if sum(c[j][chr(i + 97)] for j in range(k)) != 2 * k:
			return -1
		for j in range(k):
			if c[j][chr(i + 97)] > 1:
				return -1
	diff = [0] * (1 + n)
	for j in range(k):
		for i in range(n):
			diff[i + 1] = diff[i]
			if s[j][i] != s[0][i]:
				diff[i + 1] += 1
	return next(
		(
			''.join(
				[
					s[0][i] if diff[i] == 0 else s[0][n - 1 - i]
					for i in range(n)
				]
			)
			for i in range(n - 1)
			if diff[i + 1] == 2 + diff[i]
		),
		-1,
	)


print(solve())
