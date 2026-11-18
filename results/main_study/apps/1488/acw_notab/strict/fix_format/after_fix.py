from fractions import *


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans1 = 0
    pres = a[0]
    for i in range(1, n):
        ans1 += i * a[i] - pres
        pres += a[i]
    ans1 *= 2
    tmp = ans1 + pres
    tmp1 = n
    s = Fraction(tmp, tmp1)
    print(s.numerator, s.denominator)


solve()
