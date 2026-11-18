#!/usr/bin/env python3

from math import sqrt

primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
]

psq = [p * p for p in primes]


def sqfree(x):
    if x == 0:
        return x
    y = 1
    for p, pp in zip(primes, psq):
        while x % pp == 0:
            x = x // pp
        if 0 == x % p:
            x = x // p
            y = y * p
        if abs(x) < p:
            break
    if not int(sqrt(abs(x))) ** 2 == abs(x):
        return x * y
    else:
        return y if x > 0 else -y


n = int(input().strip())
ais = list(map(int, input().strip().split()))
bis = list(map(sqfree, ais))


prev = [-1 for i in range(n)]
last = {}


for i, b in enumerate(bis, 0):
    if b in last:
        prev[i] = last[b]
    last[b] = i

res = [0 for i in range(0, n)]
for l in range(0, n):
    cnt = 0
    for r in range(l, n):
        if 0 != bis[r] and prev[r] < l:
            cnt = cnt + 1
        res[max(cnt - 1, 0)] += 1


print(" ".join(map(str, res)))
