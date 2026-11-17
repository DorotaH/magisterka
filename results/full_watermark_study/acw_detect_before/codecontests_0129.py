from __future__ import division, print_function
import math
import sys
import os
from io import BytesIO, IOBase
#from collections import deque, Counter, OrderedDict, defaultdict
#import heapq
#ceil,floor,log,sqrt,factorial,pow,pi,gcd
#import bisect
#from bisect import bisect_left,bisect_right

BUFSIZE = 8192


class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = "x" in file.mode or "r" not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = (not b) + b.count(b"\n")
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode("ascii"))
		self.read = lambda: self.buffer.read().decode("ascii")
		self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
	"""Prints the values to a stream, or to sys.stdout by default."""
	sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
	at_start = True
	for x in args:
		if not at_start:
			file.write(sep)
		file.write(str(x))
		at_start = False
	file.write(kwargs.pop("end", "\n"))
	if kwargs.pop("flush", False):
		file.flush()


if sys.version_info[0] < 3:
	sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
	sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")


def I():
	return (int(input()))


def lint():
	return (list(map(int, input().split())))


def insr():
	s = input().strip()
	return list(s[:])


def invr():
	return (map(int, input().split()))


import itertools
from sys import maxsize, stdout, stdin, stderr
mod = int(1e9 + 7)
import sys
# def I(): return int(stdin.readline())
# def lint(): return [int(x) for x in stdin.readline().split()]
def S(): return list(map(str, input().strip()))


def grid(r, c):
	return [lint() for _ in range(r)]


from collections import defaultdict, Counter, deque
import math
import heapq
from heapq import heappop , heappush
import bisect
from math import factorial, inf
from itertools import groupby
from itertools import permutations as comb


def gcd(a, b): 
	while b:
		a %= b
		tmp = a
		a = b
		b = tmp
	
	return a


def lcm(a, b): 
	return a  // gcd(a, b) * b


def check_prime(n):
	return all(n % i for i in range(2, 1 + int(n ** (1 / 2))))


def nCr(n, r):

	return (fact(n) // (fact(r)
				* fact(n - r)))

# Returns factorial of n


def fact(n):

	res = 1
	
	for i in range(2, 1 + n):
		res = i * res
		
	return res


def primefactors(n):
	num = 0
	
	while n % 2 == 0:
		num += 1
		n = n / 2
	
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		
	
		while n % i == 0:
			num += 1
			n = n // i
			
	
	if 2 < n:
		num += 1
	return num


'''
def iter_ds(src):
	store=[src]
	while len(store):
		tmp=store.pop()
		if not vis[tmp]:
			vis[tmp]=True
			for j in ar[tmp]:
				store.append(j)
'''


def ask(a, b, c):
	# print('? 1 {}'.format(a),flush=True)
	print(c, a, b, flush=True)
	return I()


def linear_sieve(n):
	is_composite = [False] * n
	prime = []
	for i in range(2, n):
		if not is_composite[i]:
			prime.append(i)
		for j in prime:
			is_composite[i * j] = True
			if i % prime == 0:
				break
	return prime


def dfs(i, p, d):
	
	a, tmp = 0, 0
	for j in d[i]:
	    if j != p:
	        a += 1
	        tmp += dfs(j, i)

	return 0 if a == 0 else tmp / a + 1 


def primeFactors(n):
	l = []
	
	while n % 2 == 0:
		l.append(2)
		n = n // 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		
		
		while n % i == 0:
			l.append(i)
			n = n // i

	if 2 < n:
		l.append(n)
	return l


#  Sieve
d = []
primes = []
prim = [0] * (10**5 + 1)


def sieve(n):
	
	for i in range(n):
		d.append(i)

	for i in range(2, n):

		if d[i] == i:
			prim[i] = 1
			primes.append(i)
		j = 0
		while len(primes) > j and d[i] >= primes[j] and i * primes[j] < n:
		
			d[i * primes[j]] = primes[j]
			j += 1

		
def primeFactors(n):
	factors = []
	while n != 1:
		factors.append(d[n])
		n //= d[n]
	
	return factors


mod = 1000000007

t = 1
t = I()
for _ in range(t):
	n = I()
	s = lint()
	ans = 0
	k = sum(s) / n

	d = defaultdict(lambda: 0)
	for i in range(n):
	    d[s[i]] += 1
	for i in range(n):
		if (2 * k - s[i]) % 1 != 0:
		    continue
		tmp = d[int(2 * k - s[i])]
		if tmp > 0:
			ans += tmp - 1 if s[i] == k else tmp
	print(ans // 2)
		
