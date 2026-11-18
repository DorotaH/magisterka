
from queue import Queue
import sys
import math
import os.path

# CONFIG
sys.setrecursionlimit(10**9)

# LOG


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# INPUT
def ni():
    return list(map(int, input().split()))


def nio(offset):
    return [offset + int(x) for x in input().split()]


def nia():
    return list(map(int, input().split()))


# CONVERT
def toString(aList, sep=" "):
    return sep.join(str(x) for x in aList)


def mapInvertIndex(aList):
    return {k: v for v, k in enumerate(aList)}


def countMap(arr):
    m = {}
    for x in arr:
        m[x] = 1 + m.get(x, 0)
    return m


def sortId(arr):
    return sorted(list(range(arr)), key=lambda k: arr[k])

# MAIN


n, k = ni()
c = nia()
f = nia()
h = [0] + (nia())

cc = countMap(c)
cf = countMap(f)

n1 = 1 + n
k1 = k + 1

nk1 = k * n + 1
dp = [[0] * nk1 for _ in range(n1)]


for ni in range(1, n1):
    for ki in range(1, nk1):
        mficount = 1 + min(k, ki)        
        for kii in range(mficount):
            # log(ni,ki, kii, dp[ni][ki], dp[ni-1][ki-kii] + h[kii])
            dp[ni][ki] = max(dp[ni][ki], dp[ni - 1][ki - kii] + h[kii])
    # log(dp[ni])

res = sum(dp[fv][cc.get(fk, 0)] for fk, fv in list(cf.items()))
print(res)
