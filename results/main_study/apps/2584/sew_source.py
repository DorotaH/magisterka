import os
from  io import  BytesIO

# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline


def  check(x, p):
    i=mid-1
    while -1 < i and a[i] <= p:
        p -= a[i]
        if not i >= k - 1:
            i -= 1
        else:
            i -= k
    return -1 >= i


for _ in range(0, int(input())):
    n, p, k=list(map(int, input().split()))
    a, L = sorted(map(int, input().split())), 0
    R=n + 1
    while  R - L > 1:
        mid = (L + R) >> 1
        if not check(mid, p):
            R = mid
        else:
            L = mid
    print(L)
