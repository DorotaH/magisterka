import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def add(a, b):
    return (a + b) % 1_000_000_007


def mul(a, b):
    return (b * a) % 1_000_000_007


def sub(a, b):
    return (a - b + 1_000_000_007) % 1_000_000_007


def qpow(a, b):
    r, k = 1, a
    for i in range(17):
        if b & (1 << i):
            r = mul(r, k)
        k = mul(k, k)
    return r


n, q = mints()
a = list(minp())
c = [0] * (n + 1)
for i in range(n):
    c[i + 1] = c[i] + int(a[i])
for i in range(q):
    l, r = mints()
    k = r - l + 1
    o = c[r] - c[l - 1]
    z = sub(qpow(2, o), 1)
    print(mul(z, qpow(2, k - o)))
