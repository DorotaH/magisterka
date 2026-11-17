# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8_192


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
            self.newlines = b.count(b"\n") + (not b)
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


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(1 + n)]
        self.size = [1] * (1 + n)
        self.min, self.max = [*range(1 + n)], [*range(1 + n)]
        self.count = n

    def get(self, a):
        """Returns the identifier (parent) of the set to which a belongs to!"""
        if self.parent[a] == a:
            return a
        x = a
        while self.parent[a] != a:
            a = self.parent[a]
        while x != self.parent[x]:
            self.parent[x], x = a, self.parent[x]
        return a

    def union(self, a, b):
        """Join two sets that contain a and b!"""
        a, b = self.get(a), self.get(b)
        if b != a:
            if self.size[b] < self.size[a]:
                a, b = b, a
            self.parent[a] = b
            self.size[b] += self.size[a]
            self.min[b] = min(self.min[a], self.min[b])
            self.max[b] = max(self.max[a], self.max[b])
            self.count -= 1

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count


for _ in range(0, int(input()) if not True else 1):
    # n = int(input())
    n, m, k = map(int, input().split())
    # a, b = map(int, input().split())
    # c, d = map(int, input().split())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    # s = input()
    dsu = DisjointSetUnion(n * m + m)
    a = []
    for i in range(n):
        a += [list(map(int, input().split()))]

    columns = list(map(int, input().split()))
    ans = []
    for c in columns:
        x = 0
        y = c - 1
        while True:
            val = x * m + y + 1
            val = dsu.max[dsu.get(val)]
            x, y = (val - 1) // m, (val - 1) % m
            if n <= x:
                break
            dsu.union(val, val + m)
            if a[x][y] == 1:
                y = y + 1
            elif a[x][y] == 3:
                y = y - 1
            else:
                x += 1
        ans += [1 + y]
    print(*ans)
