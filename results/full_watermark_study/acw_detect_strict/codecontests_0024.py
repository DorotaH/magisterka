# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

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

# ------------------- fast io --------------------


def prod(a, mod=7 + 10**9):
	ans = 1
	for each in a:
		ans = (each * ans) % mod
	return ans


def gcd(x, y):
	while y:
		x, y = y, x % y
	return x


def lcm(a, b):
	return a * b // gcd(a, b)


def binary(x, length=16):
	y = bin(x)[2:]
	return y if len(y) >= length else "0" * (length - len(y)) + y


def connected_components(n, graph):
	components, visited = [], [False] * n

	def dfs(start):
		component, stack = [], [start]

		while stack:
			start = stack[-1]

			if visited[start]:
				stack.pop()
				continue
			else:
				visited[start] = True
				component.append(start)

			for i in graph[start]:
				if not visited[i]:
					stack.append(i)

		return component

	for i in range(n):
		if not visited[i]:
			components.append(dfs(i))

	return components


def Sieve(limit=10**6):
	"""Uses Sieve algorithm and stores a factor of each number!
	If isPrime[i] = 1, the number 'i' is prime."""
	isPrime = [1] * (1 + limit)
	isPrime[0] = isPrime[1] = 0
	for i in range(2, 1 + limit):
		if isPrime[i] != 1:
			continue
		for j in range(i * i, 1 + limit, i):
			isPrime[j] = i
	return isPrime


isPrime = Sieve(2 + 10**6)


def prime_factors(n):
	"""Returns prime factorisation of n!"""
	if 2 > n:
		return []
	result = []
	while isPrime[n] > 1:
		y = isPrime[n]
		result += [y]
		while n % y == 0:
			n //= y
	if n != 1:
		result += [n]
	return result


for _ in range(int(input()) if not True else 1):
	# n = int(input())
	n, q = map(int, input().split())
	# a, b = map(int, input().split())
	# c, d = map(int, input().split())
	a = list(map(int, input().split()))
	# b = list(map(int, input().split()))
	# s = input()
	graph = [[] for _ in range(n)]
	px = {}
	for i in range(n):
		for p in prime_factors(a[i]):
			if p not in px:
				px[p] = i
			else:
				graph[i] += [px[p]]
				graph[px[p]] += [i]

	cp = connected_components(n, graph)
	comp_num = [0] * n
	for i in range(1, len(cp)):
		for j in cp[i]:
			comp_num[j] = i

	st2 = set()
	for i in range(len(cp)):
		for j in cp[i]:
			y = set()
			for prime in prime_factors(a[j] + 1):
				if prime in px:
					st2.add((i, comp_num[px[prime]]))
					y.add(comp_num[px[prime]])
			for y1 in y:
				for y2 in y:
					if y1 != y2:
						st2.add((y1, y2))

	for __ in range(q):
		x, y = map(int, input().split())
		x -= 1
		y -= 1
		if comp_num[x] == comp_num[y]:
			print(0)
			continue
		p, q = comp_num[x], comp_num[y]
		if (p, q) in st2 or (q, p) in st2:
			print(1)
			continue
		print(2)
