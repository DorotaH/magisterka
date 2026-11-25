import math
import sys


def solve():
    n = int(input())
    a = []
    k = []
    for _ in range(n):
        A, K = map(int, input().split())
        a.append(A)
        k.append(K)

    for i in range(n):
        a[i] %= (k[i] * (a[i] // k[i]) + k[i])
    max_ = max(a)
    for i in range(n):
        a[i] %= max_
    a.sort()
    for i in range(n):
        if i % 2 == 0:
            if a[i] == 0:
                print("Takahashi")
                return
        elif 0 < a[i]:
            print("Aoki")
            return

    print("Takahashi")


solve()
