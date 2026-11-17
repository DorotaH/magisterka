# cook your dish here
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
try:
	sys.stdin, sys.stdout, sys.stderr = (
		open("input.txt"),
		open("output.txt", "w"),
		open("error.txt", "w"),
	)
except:
	pass
ii1 = lambda: int(sys.stdin.readline().strip())  # for interger
is1 = lambda: sys.stdin.readline().strip()  # for str
iia = lambda: list(map(int, sys.stdin.readline().strip().split()))  # for List[int]
isa = lambda: sys.stdin.readline().strip().split()  # for List[str]
mod = int(1e9 + 7)
from collections import *

# abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MOD = 1000000007
# sys.setrecursionlimit(500000)
###################### Start Here ######################
# from functools import lru_cache; from decimal import *;from itertools import *
# from collections import *;import bisect
# from heapq import *;

import math
from math import *

# def primeFactors(n):
#     ls = []
#     while n % 2 == 0:
#         ls.append(2)
#         n = n / 2

#     for i in range(3,int(math.sqrt(n))+1,2):
#         while n % i== 0:
#             ls.append(i)
#             n = n / i
#     if n > 2:
#         ls.append(n)
#     return ls


"""
ii1() ==> for interger
is1() ==> for str
iia() ==> for List[int]
isa() ==> for List[str]
"""


def foo(s):
	while s % 2 == 0:
		s = s / 2
		return True
	for i in range(3, int(math.sqrt(s)) + 1, 2):
		if s % i == 0:
			return True
	else:
		return False


for _ in range(ii1()):
	n = ii1()
	lt = iia()

	s = sum(lt)
	sol = [i + 1 for i in range(n)]
	# print(s,foo(s))
	if foo(s) == True:
		print(len(sol))
		print(*sol)
	else:
		odd = []
		eve = []
		for i in range(n):
			if lt[i] % 2 != 0:
				odd.append(i)
			else:
				eve.append(i)

		for i in odd:
			if foo(s - lt[i]):
				sol.remove(i + 1)
				print(len(sol))
				print(*sol)
				break
		else:
			for i in eve:
				if foo(s - lt[i]):
					sol.remove(i + 1)
					print(len(sol))
					print(*sol)
					break
