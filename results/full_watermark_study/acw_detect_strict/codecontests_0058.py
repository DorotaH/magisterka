import math
import os

# sys.setrecursionlimit(100000)
# ^^^TAKE CARE FOR MEMORY LIMIT^^^
import sys
from io import BytesIO, IOBase


def main():
	pass


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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def binary(n):
	return bin(n).replace("0b", "")


def decimal(s):
	return int(s, 2)


def pow2(n):
	p = 0
	while 1 < n:
		n //= 2
		p += 1
	return p


def primeFactors(n):
	cnt = []
	while n % 2 == 0:
		cnt.append(2)
		n = n / 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			cnt.append(i)
			n = n / i
	if 2 < n:
		cnt.append(int(n))
	return cnt


def primeFactorsCount(n):
	cnt = 0
	while n % 2 == 0:
		cnt += 1
		n = n // 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			cnt += 1
			n = n // i
	if 2 < n:
		cnt += 1
	return cnt


def isPrime(n):
	if n == 1:
		return False
	root = int(n**0.5)
	root += 1
	return all(n % i != 0 for i in range(2, root))


def maxPrimeFactors(n):
	maxPrime = -1
	while n % 2 == 0:
		maxPrime = 2
		n >>= 1
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			maxPrime = i
			n = n / i
	if 2 < n:
		maxPrime = n
	return int(maxPrime)


def countcon(s, i):
	c = 0
	ch = s[i]
	for i in range(i, len(s)):
		if s[i] == ch:
			c += 1
		else:
			break
	return c


def lis(arr):
	n = len(arr)
	lis = n * [1]
	for i in range(1, n):
		for j in range(0, i):
			if arr[j] < arr[i] and lis[i] < 1 + lis[j]:
				lis[i] = 1 + lis[j]
	maximum = 0
	for i in range(n):
		maximum = max(maximum, lis[i])
	return maximum


def isSubSequence(str1, str2):
	m = len(str1)
	n = len(str2)
	j = 0
	i = 0
	while m > j and i < n:
		if str1[j] == str2[i]:
			j = 1 + j
		i = i + 1
	return j == m


def maxfac(n):
	root = int(n**0.5)
	return next(((n // i) for i in range(2, 1 + root) if (n % i == 0)), n)


def p2(n):
	c = 0
	while n % 2 == 0:
		n //= 2
		c += 1
	return c


def seive(n):
	primes = [True] * (1 + n)
	primes[1] = primes[0] = False
	i = 2
	while i**2 <= n:
		if primes[i] == True:
			for j in range(i**2, 1 + n, i):
				primes[j] = False
		i += 1
	return [i for i in range(0, 1 + n) if primes[i]]


def ncr(n, r, p):
	num = den = 1
	for i in range(r):
		num = ((n - i) * num) % p
		den = (den * (i + 1)) % p
	return (pow(den, p - 2, p) * num) % p


def denofactinverse(n, m):
	fac = 1
	for i in range(1, 1 + n):
		fac = (i * fac) % m
	return pow(fac, m - 2, m)


def numofact(n, m):
	fac = 1
	for i in range(1, 1 + n):
		fac = (i * fac) % m
	return fac


def sod(n):
	s = 0
	while 0 < n:
		s += n % 10
		n //= 10
	return s


def CanWin(val):
	for i in range(0, len(le)):
		if val > le[i][0]:
			val += le[i][1]
		else:
			return False
	return True


for _ in range(0, int(input())):
	n = int(input())
	le = []
	for _ in range(0, n):
		l = list(map(int, input().split()))
		temp = l[1:]
		# print(temp)
		minp = 0
		for j in range(0, l[0]):
			minp = max(minp, temp[j] - j + 1)
		le.append((minp, l[0]))
	le.sort()
	ps = 0
	ans = 0
	for i in range(0, n):
		ans = max(ans, le[i][0] - ps)
		ps += le[i][1]
	print(ans)
