from fractions import *


def solve():
    n, a = int(input()), list(map(int,input().split()))
    a.sort()
    ans1, pres = 0, a[0]
    for  i in  range(1,n):
        ans1 += i*a[i] -pres
        pres += a[i]
    ans1 = ans1 * 2
    tmp, tmp1 = pres+ans1, n
    s=Fraction(tmp,tmp1)
    print(s.numerator,s.denominator)

solve()
