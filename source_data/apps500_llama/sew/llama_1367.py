import sys
input = sys.stdin.readline

def  factorial(n):
    f=[1]*(n + 1)
    for  i in  range(2, n + 1):
        f[i]=(f[i-1] * i)%mod
    return  f

mod = 10**9 + 7
factorial_mod = factorial(10**5)

def  choose(n, k):
    return  (factorial_mod[n]*pow(factorial_mod[k], -1, mod)*pow(factorial_mod[n-k], -1, mod))%mod

def  solve():
    n, f=map(int, input().split())
    ans=0
    for  a in  range(1, n):
        if n - a < f:
            break
        if 0 == (n - a) % f:
            ans = ans + choose(n - 1, a - 1)
            ans = ans % mod
    return  ans

for  _ in  range(int(input())):
    print(solve())
