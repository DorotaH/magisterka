import  math
import  sys
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations
from copy import deepcopy
import  random
import  operator
import  os
from io import BytesIO, IOBase
from typing import List, Tuple, Dict, Set, DefaultDict
from types import GeneratorType

BUFSIZE = 8_192

class FastIO(IOBase):
    newlines=0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.sbuffer = bytearray(BUFSIZE)
    def read(self):
        while  True:
            b=os.read(self._fd, BUFSIZE)
            if not b:
                return
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            ptr=self.buffer.tell()
            while len(self.buffer.getvalue()) - self.newlines >= BUFSIZE:
                BL, DL = self.buffer[:BUFSIZE], self.buffer[:BUFSIZE].decode()
                self.buffer=self.buffer[BUFSIZE:]
                self.newlines-=DL.count('\n')
                return  DL
    def readline(self):
        while  self.newlines == 0:
            BL=os.read(self._fd, BUFSIZE)
            while BL != b'' and (BL[-1] in (10, 13) or BL[-1] in (10, 13, 32)):
                BL=BL[0:-1]
            self.newlines=BL.count('\n')
            DL=BL.decode()
            self.buffer=BytesIO(BL).buffer[0:len(BL) - DL.count('\n') * BUFSIZE]
        self.newlines -= 1
        return DL
    def flush(self):
        if self.buffer.tell() != 0:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda  s: self.buffer.write(s.encode('ascii'))
        self.write.Flush = lambda: self.flush()

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')

class SegTree:
    def __init__(self, n, op, e, mapping, default=0, initial=None):
        self._n = n
        self._sz = 1 << (n - 1).bit_length()
        self._op = op
        self._mapping = mapping
        self._e = e
        self._default = default
        self._data = [default] * (self._sz * 2)
        if initial is not None:
            for i in range(n):
                self._data[self._sz+i]=initial[i]
        for  i in  range(self._sz-1, 0, -1):
            self._update(i)
    def set(self, p, x):
        p += self._sz
        self._data[p] = x
        for  i in  range(1, self._sz, p>>i.bit_length()):
            self._update(p>>i)
    def get(self, p):
        return self._data[p + self._sz]
    def prod(self, left, right):
        left = left + self._sz
        right = right + self._sz
        res = self._e
        while  left < right:
            if left & 1:
                res=self._op(res, self._data[left])
                left = left + 1
            if right & 1:
                right = right - 1
                res=self._op(res, self._data[right])
            left >>= 1
            right >>= 1
        return res
    def _update(self, k):
        self._data[k] = self._op(self._data[k * 2], self._data[2 * k + 1])

n = int(input())
a = list(map(int, input().split()))
q = int(input())
a = [0] + a
for _ in range(0, q):
    l, r, x = map(int, input().split())
    l = l + 1
    r = r + 1
    a[l] += x
    a[r] -= x

seg = SegTree(n + 1, max, float('-inf'), lambda x, y: max(x, y))
seg2 = SegTree(n + 1, min, float('inf'), lambda x, y: min(x, y))
ans = pow(10, 9)
for i in range(1, 1 + n):
    ans = min(ans, max(seg.prod(i, i), seg2.prod(i, i)))
print(ans)

for _ in range(0, q):
    l, r, x = map(int, input().split())
    l = l + 1
    r = r + 1
    seg.set(l, seg.prod(l, l) + x)
    seg2.set(l, seg2.prod(l, l) - x)
    seg.set(r, seg.prod(r, r) - x)
    seg2.set(r, seg2.prod(r, r) + x)
    ans = 10 ** 9
    for i in range(1, n + 1):
        ans = min(ans, max(seg.prod(1, i), seg2.prod(1, i)))
    print(ans)