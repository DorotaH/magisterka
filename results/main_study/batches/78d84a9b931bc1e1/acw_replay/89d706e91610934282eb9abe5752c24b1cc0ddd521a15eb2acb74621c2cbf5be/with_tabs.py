# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:42:34 2017

@author: Sean38
"""


n = int(input().rstrip())
s = input()
a = [int(ch) for ch in s.split()]
a = a[:n]
a.sort()


def check_num(p, i):

	# i = ap + b(p+1)
	# min(a+b) <=> max(b)
	# b(p+1) <= i
	# b == i (mod p)
	max_b = i // (1 + p)
	b = i % p + ((max_b - i % p) // p) * p
	# cur = a + b
	cur = (i - b) // p

	# print(cur - b, b, p)
	return None if 0 > b else cur


def sets_num(p):

	total = 0
	for i in a:
		if check_num(p, i):
			total += check_num(p, i)
		else:
			return None
	return total


for div_sets in range(1, a[0] + 1):
	p, q = divmod(a[0], div_sets)
	if q == 0:
		if sets_num(p):
			print(sets_num(p))
			break
		if (0 < p) and sets_num(p - 1):
			print(sets_num(p - 1))
			break
	elif sets_num(p):
		print(sets_num(p))
		break
