from math import *
from decimal import *
from decimal import Decimal as D
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
from itertools import *
from itertools import permutations as perm
from itertools import product as prod
from sys import *
ip = input
ra = lambda: list(map(int, input().split()))
ri = lambda: int(input())
rd = lambda: map(int, input().split())
MOD = 10 ** 9 + 7
MOD2 = 998244353
maxn = 10 ** 6 + 10
N = 10 ** 5 + 10
N2 = 2 * 10 ** 5
getcontext().prec = 20


def debug(*a):
	stderr.write(' '.join(map(str, a)) + '\n')


def fp(x, p, m):
	r = 1
	while p:
		if p % 2:
			r = r * x % m
			p -= 1
		else:
			x = x * x % m
			p //= 2
	return r


def fact(x, m):
	r = 1
	for i in range(2, x + 1):
		r = r * i % m
	return r


def C(n, k, m):
	return fact(n, m) * fp(fact(n - k, m), m - 2, m) % m * fp(fact(k, m), m - 2, m) % m


class SegmentTree:
	def f(self, a, b):
		return a + b

	def __init__(self, n, a):
		self.tree = [0] * (2 * n)
		self.n = n
		for i in range(n):
			self.tree[n + i] = a[i]
		for i in range(n - 1, 0, -1):
			self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

	def q(self, l, r):
		l += self.n
		r += self.n
		res = 0
		while r > 1:
			if l % 2:
				res = self.f(res, self.tree[l]) 
				l += 1
			if r % 2:
				r -= 1
				res = self.f(res, self.tree[r])
			r //= 2
			l //= 2
		return res

	def u(self, index, value):
		index += self.n
		self.tree[index] = value
		index //= 2
		while index > 0:
			self.tree[index] = self.f(self.tree[2 * index], self.tree[2 * index + 1])
			index //= 2


def z_function(s):
	l, r, n = 0, 0, len(s)
	z = [0] * n
	z[0] = 0
	for i in range(1, n):
		if r >= i: z[i] = min(z[i - l], r - i + 1)
		while z[i] + i < n and s[z[i]] == s[z[i] + i]: z[i] += 1
		if i + z[i] - 1 > r:
			l = i
			r = l + z[i] - 1
	return z


def pc_pre(a):
	n = len(a)
	r = [0] * (n + 1)
	for i in range(n):
		r[i + 1] = r[i] + a[i]
	return r


def pc_suf(a):
	n = len(a)
	r = [0] * (n + 1)
	for i in range(n - 1, -1, -1):
		r[i] = r[i + 1] + a[i]
	return r


def bsloe(a, v):
	l, h = -1, len(a)
	while h - l > 1:
		m = (h + l) // 2
		if a[m] > v: h = m
		else: l = m
	return l


def bsh(a, v):
	l, h = -1, len(a)
	while h - l > 1:
		m = (h + l) // 2
		if a[m] > v: h = m
		else: l = m
	return h


def precalc_fact(n):
	global F
	F = [1] * (n + 1)
	for i in range(2, n + 1):
		F[i] = F[i - 1] * i


def precalc_fact_mod(n, m):
	global F
	F = [1] * (n + 1)
	for i in range(2, n + 1):
		F[i] = F[i - 1] * i % m


def test():
	a = [1, 2, 3]
	s = 'abcabcab'
	assert (C(3, 2, 5) == 3)
	assert (pc_pre(a) == [0, 1, 3, 6])
	assert (pc_suf(a) == [6, 5, 3, 0])
	assert (z_function(s) == [0, 0, 0, 5, 0, 0, 2, 0])
	assert (fp(2, 3, 5) == 3)
	assert (fact(3, 5) == 1)
	t = SegmentTree(3, a)
	assert (t.q(1, 3) == t.f(a[1], a[2]))
	t.u(0, 5)
	assert (t.q(0, 2) == t.f(5, a[1]))
	assert (bsh(a, 3) == 3)
	assert (bsloe(a, 3) == 2)
	debug("tests passed")


test()
################    code goes here    ################


def calcsums(a):
	r = set([0])
	for i in a:
		nr = set()
		for j in r:
			nr.add(j)
			nr.add(j + i)
			nr.add(j - i)
		r = nr
	return r


def chk(a, i):
	b = a[:i] + a[i + 1:]
	return a[i] in calcsums(b)


def solve(n, a):
	*a, = map(abs, a)
	for i in range(n):
		if chk(a, i):
			print('YES')
			return
	print('NO')


t, = rd()
for _ in range(t):
	n, = rd()
	a = ra()
	solve(n, a)
