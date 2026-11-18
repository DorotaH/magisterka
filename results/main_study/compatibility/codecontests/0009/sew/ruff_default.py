# from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
# from bisect import bisect_right as br               #c++ upperbound br(array,element)
# from __future__ import print_function, division    #while using python2
# from itertools import accumulate
# from collections import defaultdict, Counter


def modinv(n, p):
    return pow(n, p - 2, p)


def solve():
    n, m, k = [int(x) for x in input().split()]
    vert_k, arr = (n * m) // 2 - k, [[0 for i in range(m)] for j in range(n)]
    j1, j2 = [0, 1]

    if 1 == n % 2:
        for j in range(0, m, 2):
            if k > 0 and j + 1 < m:
                arr[0][j] = arr[0][j + 1] = "h"
                k = k - 1

    while m > j2 and k > 0:
        for i in range(n):
            if arr[i][j1] == "h":
                continue
            if k == 0:
                break
            elif k == 1:
                if not (n - i - 1) % 2 == 0:
                    break
                else:
                    arr[i][j1] = arr[i][j2] = "h"
                    k -= 1
            else:
                arr[i][j1] = arr[i][j2] = "h"
                k = k - 1
            # if i < n-2:
            #     arr[i][j1] = 'h'
            #     arr[i][j2] = 'h'
            #     k -= 1
            # elif (i == n-2 and k > 1):
            #     arr[i][j1] = 'h'
            #     arr[i][j2] = 'h'
            #     arr[i+1][j1] = 'h'
            #     arr[i+1][j2] = 'h'
            #     k -= 2
            #     break
            # elif i == n-1:
            #     arr[i][j1] = arr[i][j2] = 'h'
            #     k -= 1
        j1 = j2 + 1
        j2 = j1 + 1

    k = vert_k
    # print("vert", k)
    i1, i2 = [0, 1]
    while n > i2 and k > 0:
        for j in range(m):
            if k == 0:
                break
            if arr[i1][j] == 0 and arr[i2][j] == 0:
                arr[i1][j] = arr[i2][j] = "v"
                k = k - 1
        i1 = i2
        i2 = i1 + 1

    ct = 0
    for x in arr:
        ct += x.count(0)
        # print(*x)
    if ct == 0:
        print("YES")
    else:
        print("NO")


def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    for case in range(int(input())):
        solve()


# ------------------ Python 2 and 3 footer by Pajenegod and c1729-----------------------------------------
py2 = round(0.5)
if py2:
    range = xrange

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(BytesIO):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super().write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0, 2), super().write(s))[0])
        return s

    def read(self):
        while self._fill():
            ...
        return super().read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill()
            self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super().readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if not py2:
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
        else:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()
