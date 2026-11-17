#!/usr/bin/env python3
# from typing import *

import sys
import io
import math
import collections
import decimal
import itertools
import bisect
import heapq

def  input():
    return  sys.stdin.readline()[:-1]


# sys.setrecursionlimit(1000000)

# _INPUT = """2 4
# 1 3
# 1 2
# """
# sys.stdin = io.StringIO(_INPUT)

INF = 10**10

MOD = 998244353

def  solve(d):
    M1 = M // d

    dp = [0] * (M1+1)
    dp[0] = 1
    for  i in  range(0, N):
        s = [0]
        for  v in  dp:
            s.append((s[-1]+v)%MOD)
        l, r = T[i]
        l1, r1 = math.ceil(l/d), r//d
        for  m in  range(M1+1):
            l2, r2 = max(m-r1, 0), max(m-l1+1, 0)
            dp[m]=(s[r2]-s[l2])%MOD

    return  sum(dp[1:])%MOD

def  Mobius(n):
    s = set()
    while  n>1:
        if  D[n] in  s:
            return 0
        s.add(D[n])
        n = n // D[n]
    if len(s) % 2 == 0:
        return 1
    else:
        return -1

N, M = map(int, input().split())
T = []
for  _ in  range(0, N):
    l, r=map(int, input().split())
    T.append((l, r))

A_MAX = M
D = [0] * (1 + A_MAX)
for  i in  range(2, 1 + A_MAX):
    if  D[i] == 0:
        D[i]=i
        n=i*i
        while  n <= A_MAX:
            D[n]=i
            n+=i

Table, ans = [0] * (M+1), 0
for  d in  range(1, 1+M//N):
    mo=Mobius(d)
    if  mo == 0:
        continue
    v=solve(d)
    ans=(ans+mo * v)%MOD
    # print(d, v, n)
print(ans)