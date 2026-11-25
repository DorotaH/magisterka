import math
import sys
from collections import Counter


def solve():
    n, k=map(int, input().split())
    a=list(map(int, input().split()))

    total_sum, ways = sum(a[i] * 2**i for i in range(n + 1)), 0

    for  i in  range(0, n):
        a_i = a[i]
        if total_sum - (2 * a_i) <= 0:
            continue
        if k >= -a_i:
            ways += 1
        if k >= a_i:
            ways += 1

    print(ways)

if  __name__=="__main__":
    solve()
