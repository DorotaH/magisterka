# SHRi GANESHA    author: Kunal Verma #

import os
import sys
from  collections import  defaultdict, Counter

from  io import  BytesIO, IOBase
from  math import  gcd


def  lcm(a, b):
    return (a * b) // gcd(a, b)


'''
    mod = 10 ** 9 + 7
    fac = [1]
    for i in range(1, 2 * 10 ** 5 + 1):
        fac.append((fac[-1] * i) % mod)
    fac_in = [pow(fac[-1], mod - 2, mod)]
    for i in range(2 * 10 ** 5, 0, -1):
        fac_in.append((fac_in[-1] * i) % mod)
    fac_in.reverse()
    def comb(a, b):
        if a < b:
            return 0
        return (fac[a] * fac_in[b] * fac_in[a - b]) % mod
'''


# MAXN = 10000004
# spf = [0 for i in range(MAXN)]
# adj = [[] for i in range(MAXN)]
def  sieve():
    global  spf, adj, MAXN
    spf[1] = 1
    for  i in  range(2, MAXN):
        spf[i] = i

    for  i in  range(2, MAXN):
        if  i * i > MAXN:
            break
        if  (spf[i] == i):
            for  j in  range(i*i, MAXN, i):
                if  (spf[j] == j):
                    spf[j] = i


def  getdistinctFactorization(n):
    global  adj, spf, MAXN
    for  i in  range(1, 1 + n):
        index, x = 1, i
        if  (1 != x):
            adj[i].append(spf[x])
        x = x // spf[x]
        while (x != 1):
            if  (adj[i][index - 1] != spf[x]):
                adj[i].append(spf[x])
                index += 1
            x //= spf[x]
def  printDivisors(n):
    i, z = 2, [1, n]
    while  i<=sqrt(n):
        if (n % i == 0):
            if not (n / i == i):
                z.append(i)
                z.append(n // i)
            else:
                z.append(i)
        i += 1
    return z


def  create(n, x, f):
    pq = len(bin(n)[2:])
    tt, dp = min if f == 0 else max, [[inf] * n for _ in range(pq)]
    dp[0] = x
    for  i in  range(1, pq):
        for  j in  range(n - (1 << i) + 1):
            dp[i][j]=tt(dp[i-1][j], dp[i-1][j+(1<<(i-1))])
    return dp


def  enquiry(l, r, dp, f):
    if r < l:
        return inf if not f else -inf
    tt, pq1 = max if f == 1 else min, len(bin(r - l + 1)[2:]) - 1
    return tt(dp[pq1][l], dp[pq1][r - (1 << pq1) + 1])
def  SieveOfEratosthenes(n):
    prime, p = [True for i in range(n + 1)], 2
    while  (p*p<=n):
        if (prime[p] == True):
            for  i in  range(p*p, n + 1, p):
                prime[i] = False
        p += 1
    x = []
    for  i in  range(2, 1 + n):
        if  prime[i]:
            x.append(i)
    return x





def  main():

    n,m = map(int,input().split())
    s, dp=[input().strip() for i in range(n)], [0]*(m)





    for  i in  range(m - 1,0,-1):
        for  j in  range(1,n):
            if  s[j-1][i]=='X' and  s[j][i-1]=="X":
                dp[i]=1

    for  i in  range(1,m):
        dp[i] += dp[i - 1]

    for  i in  range(0, int(input())):

        xx,yy = map(int,input().split())
        if not xx==yy:
            yy-=1
            xx-=1
            if dp[yy]-dp[xx]>0:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
# Fast IO Region
BUFSIZE = 8_192


class  FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="x" in  file.mode or  "r" not  in file.mode
        self.write=self.buffer.write if  self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if  not  b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not  b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class  IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda  s: self.buffer.write(s.encode("ascii"))
        self.read=lambda: self.buffer.read().decode("ascii")
        self.readline=lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__=='__main__':
    main()