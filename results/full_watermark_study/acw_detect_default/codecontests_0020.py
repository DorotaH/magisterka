# ----------FASTIOSTART-----------#
import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
	from __builtin__ import xrange as range
	from future_builtins import map
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
# ----------FASTIOFINISH----------#
from bisect import *
from collections import *
from itertools import *
from math import *
from queue import *
from re import *
from statistics import *
from string import *

# ----------SASTA_STL-------------#
# stack


class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def at(self, idx):
		try:
			return self.items[idx]
		except:
			return -1


# priority_queue


class priority_queue:
	def __init__(self):
		self.queue = []

	def __str__(self):
		return " ".join([str(i) for i in self.queue])

	def empty(self):
		return len(self.queue) == 0

	def push(self, data):
		self.queue.append(data)

	def pop(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()


# ----------SASTA_STL-------------#
mod = int(1e9 + 7)
imax = float("inf")
imin = float("-inf")
true = True
false = False
N = int(1e5)
none = None
inp = lambda: input()
I = lambda: int(inp())
M = lambda: map(int, inp().split())
MS = lambda: map(str, inp().split())
S = lambda: list(MS())
L = lambda: list(M())


def IO():
	try:
		sys.stdin = open("input.txt", "r")
		sys.stdout = open("uttar.txt", "w")
	except:
		pass


IO()
# ----------TOTKA---------#


def kabraji_ka_totka():
	# totka hai dosto !
	s = inp()
	team1 = 0
	team2 = 0
	res = 9
	res = 10
	maxa = 0
	maxb = 0
	mina = 0
	minb = 0
	for i in range(10):
		if i & 1:
			if s[i] != "0":
				maxb += 1
			if s[i] == "1":
				minb += 1
		else:
			if s[i] != "0":
				maxa += 1
			if s[i] == "1":
				mina += 1
		if (10 - i) // 2 < maxa - minb:
			res = i + 1
			break
		if (9 - i) // 2 < maxb - mina:
			res = i + 1
			break
	print(res)


# ----------TOTKA----------#
if __name__ == "__main__":
	for _ in range(I()):
		kabraji_ka_totka()
