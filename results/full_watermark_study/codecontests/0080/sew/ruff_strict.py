import sys

input = sys.stdin.readline


# sys.setrecursionlimit(400000)
def I():
    return input().strip()


def II():
    return int(input().strip())


def LI():
    return [*map(int, input().strip().split())]


# import copy, string, math, time, functools, random, fractions
from bisect import bisect_left
from collections import Counter, defaultdict


def get(a, u):
    ans = 0
    a.sort()
    arr = list()
    for i in range(len(a)):
        arr.append(bisect_left(u, a[i]))
    c = Counter(arr)
    for i in c.values():
        ans += nc2(i)
    return ans


def nc2(p):
    if p < 2:
        return 0
    return (p * (p - 1)) // 2


for _ in range(0, II()):
    n, m, k = LI()
    u = LI()
    v = LI()
    x = set(u)
    y = set(v)
    a = []
    b = []
    sx = defaultdict(lambda: [])
    sy = defaultdict(lambda: [])
    for _ in range(k):
        l, r = LI()
        if l in x and r in y:
            continue
        if l in x:
            sx[l].append(r)
            a.append(r)
        if r in y:
            sy[r].append(l)
            b.append(l)
    u.sort()
    v.sort()
    ans = get(b, u) + get(a, v)
    for a in sx.values():
        ans -= get(a, v)
    for b in sy.values():
        ans -= get(b, u)
    print(ans)
