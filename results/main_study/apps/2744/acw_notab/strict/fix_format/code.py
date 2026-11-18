py2 = round(0.5)

if py2:
    range = xrange

import os
import sys
from io import BytesIO, IOBase

# FastIO for PyPy2 and PyPy3 by Pajenegod


class FastI:
    def __init__(self, fd=0, buffersize=2**14):
        self.stream = stream = BytesIO()
        self.bufendl = 0

        def read2buffer():
            curpos = stream.tell()
            s = os.read(fd, os.fstat(fd).st_size + buffersize)
            stream.seek(0, 2)
            stream.write(s)
            stream.seek(curpos)
            return s

        self.read2buffer = read2buffer

    def read(self):
        while self.read2buffer():
            pass
        return self.stream.read() if self.stream.tell() else self.stream.getvalue()

    def readline(self):
        while self.bufendl == 0:
            s = self.read2buffer()
            self.bufendl += (not s) + s.count(b"\n")
        self.bufendl -= 1
        return self.stream.readline()

    def input(self):
        return self.readline().rstrip(b"\r\n")


class FastO(IOBase):
    def __init__(self, fd=1):
        stream = BytesIO()
        self.flush = lambda: (
            os.write(fd, stream.getvalue()) + stream.truncate(0) + stream.seek(0)
        )
        self.write = stream.write if py2 else lambda s: stream.write(s.encode())


sys.stdin, sys.stdout = FastI(), FastO()
input = sys.stdin.readline

big = 10**12 * 2


class segheap:
    def __init__(self, data):
        n = len(data)
        m = 1
        while m < n:
            m *= 2
        self.n = n
        self.m = m

        self.data = [big] * (2 * m)
        for i in range(n):
            self.data[i + m] = data[i]
        for i in reversed(range(m)):
            self.data[i] = min(self.data[i * 2], self.data[i * 2 + 1])

    def mini(self):
        i = 1
        while i < self.m:
            i = i * 2 if self.data[i] == self.data[i * 2] else i * 2 + 1
        i -= self.m
        self.setter(i, big)
        return i

    def setter(self, ind, val):
        ind += self.m
        if val < self.data[ind]:
            while ind > 0 and val < self.data[ind]:
                self.data[ind] = val
                ind //= 2
        elif val > self.data[ind]:
            old_val = self.data[ind]
            self.data[ind] = val
            ind //= 2
            while ind > 0 and self.data[ind] == old_val:
                self.data[ind] = min(self.data[2 * ind], self.data[2 * ind + 1])
                ind //= 2


s = sys.stdin.read().replace(b"\r", b"")
inp = []
numb = 0

for i in range(len(s)):
    if s[i] >= 48:
        numb = numb * 10 + s[i] - 48
    elif s[i] != 13:
        inp.append(numb)
        numb = 0
if s[-1] >= 48:
    inp.append(numb)

ind = 0

n = inp[ind]
ind += 1
m = inp[ind]
ind += 1

coupl = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for _ in range(m):
    v = inp[0 + ind] - 1
    u = inp[1 + ind] - 1
    w = inp[2 + ind]
    ind += 3
    coupl[v].append(u)
    coupl[u].append(v)
    cost[u].append(w)
    cost[v].append(w)

best = [inp[i + ind] for i in range(n)]

Q = segheap(best)

while Q.data[1] != big:
    c = Q.data[1]
    node = Q.mini()
    if best[node] != c:
        continue
    for j in range(len(coupl[node])):
        nei = coupl[node][j]
        C = c + cost[node][j] * 2
        if best[nei] > C:
            best[nei] = C
            Q.setter(nei, C)

for x in best:
    sys.stdout.write(str(x))
    sys.stdout.write("\n")
