import sys
import math
import random
import bisect
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
import os
from io import BytesIO, IOBase
import math
import itertools
import copy


class FastIO(IOBase):
    new_line = False

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.sbuf = getvalue(self._fd, 8192)

    def readline(self):
        while not self.new_line:
            alost = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.sbuf = getvalue(self._fd, 8192)
            self.buffer.seek(alost, 0)
            self.new_line = self.buffer.read().decode().rstrip("\r\n")
        self.new_line = False
        return self.new_line

    def flush(self):
        if self.buffer.tell():
            self.buffer.seek(0)
            os.write(self._fd, self.buffer.getvalue())


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.writeall = lambda s: self.buffer.write(s.encode("ascii"))
        self.readline = self.buffer.readline
        self.readline()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


class LazySegTree:
    def __init__(self, data, default=0, func=gcd):
        """initialize the lazy SegTree with data. default is a function or a constant,
        and func is a function or an operation"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = pow2(ceil(log2(_len_)))
        self.data = [default] * (2 * self._size)
        self.lazy = [0] * (2 * self._size)
        for i in range(self._len):
            self.data[self._size + i] = data[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)
        self._update = staticmethod(self._update)
        self._clear_lazy = staticmethod(self._clear_lazy)
        self._push = staticmethod(self._push)
        self._all = staticmethod(self._all)

    def _update(self, k):
        self.data[k] = self._func(self.data[2 * k], self.data[2 * k + 1])

    def _clear_lazy(self, k):
        self.data[k] += self.lazy[k]
        self.lazy[k] = 0

    def _push(self, k):
        if self.lazy[k]:
            self.lazy[2 * k] += self.lazy[k]
            self.lazy[2 * k + 1] += self.lazy[k]
            self.lazy[k] = 0

    def update(self, start, stop, value):
        self._clear_lazy(start + self._size)
        self._clear_lazy(stop + self._size)
        start += self._size
        stop += self._size
        while start < stop:
            if start % 2 == 1:
                self._push(start)
                self.data[start] += value
                start += 1
            if stop % 2 == 0:
                self._push(stop - 1)
                self.data[stop - 1] += value
            start >>= 1
            stop >>= 1

    def query(self, start, stop):
        start += self._size
        stop += self._size
        self._push(start)
        self._push(stop - 1)
        ans = self._default
        while start < stop:
            if start % 2 == 1:
                ans = self._func(ans, self.data[start])
                start += 1
            if stop % 2 == 0:
                ans = self._func(ans, self.data[stop - 1])
            start >>= 1
            stop >>= 1
        return ans

    def __str__(self):
        for i in range(self._size - 1, 0, -1):
            self._update(i)
        return " ".join(map(str, self.data[self._size :]))


class LazySegTreeMax(LazySegTree):
    def _update(self, k):
        self.data[k] = max(self.data[2 * k], self.data[2 * k + 1])


n, q = map(int, input().split())
k = [0] * (2 * 10**5)
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i], k[int(input().split()[1]) - 1] = map(int, input().split())
s = LazySegTreeMax(k, 0, max)
for i in range(q):
    c, d = map(int, input().split())
    s.update(int(c) - 1, int(c), -a[c])
    s.update(int(d) - 1, int(d), a[c])
    s.update(int(d) - 1, int(d), a[c])
    print(s.query(int(d) - 1, int(d)))
