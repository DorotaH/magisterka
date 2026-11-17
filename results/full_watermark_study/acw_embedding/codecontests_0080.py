import math
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(400000)
def I(): return input().strip()
def II(): return int(input().strip())
def LI(): return [*map(int, input().strip().split())]
# import copy, string, math, time, functools, random, fractions
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter, OrderedDict
from itertools import permutations, chain, combinations, groupby
from operator import itemgetter
from types import GeneratorType  # for recursion
from typing import Iterable, TypeVar, Union  # for sorted set


def get(a, u):
    a.sort()
    arr = [bisect_left(u, a[i]) for i in range(len(a))]
    c = Counter(arr)
    return sum(nc2(i) for i in c.values())


def nc2(p):
    return 0 if p < 2 else (p * (p - 1)) // 2


for _ in range(II()):
    n, m, k = LI()
    u = LI()
    v = LI()
    x = set(u)
    y = set(v)
    a, b = [], []
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





