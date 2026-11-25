import os
import sys
from decimal import *
from io import BytesIO, IOBase

BUFSIZE = 8192
inf = float("inf")
eps = 1e-6


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.writable and self.unseekable

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
            self.newlines = b.count(b"\n") + (not b)
            if not b:
                return b
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


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def update(self, x, v):
        while x <= self.n:
            self.t[x] += v
            x += x & -x

    def pref_sum(self, x):
        res = 0
        while x:
            res += self.t[x]
            x -= x & -x
        return res

    def range_sum(self, l, r):
        return self.pref_sum(r) - self.pref_sum(l - 1)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
fen = FenwickTree(n + 1)
for i in range(n):
    fen.update(i + 1, a[i])

for _ in range(m):
    t = int(input())
    if t == 1:
        x, y, k = map(int, input().split())
        fen.update(x, a[x - 1])
        fen.update(x + k, -a[x - 1])
        a[x] = a[x - 1] + fen.range_sum(x, x + k) - fen.range_sum(x - 1, x)
        b[y - 1] = a[y - 1] + fen.range_sum(y, y + k) - fen.range_sum(y - 1, y)
    else:
        x = int(input())
        print(b[x - 1])
