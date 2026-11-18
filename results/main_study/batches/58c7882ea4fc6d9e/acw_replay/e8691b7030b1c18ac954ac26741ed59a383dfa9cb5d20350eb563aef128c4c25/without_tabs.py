#!/usr/bin/env python3


def ri():
    return list(map(int, input().split()))


m = 7 + 10**9
s = input()
n = len(s)
o = [0 for _ in range(len(s))]
c = [0 for _ in range(len(s))]
fac = [0 for _ in range(n)]

fac[0] = 1
for i in range(1, n):
    fac[i] = fac[i - 1] * i % m

invfac = [pow(fac[i], m - 2, m) for i in range(n)]
if s[0] == "(":
    o[0] = 1
for i in range(1, n):
    o[i] = 1 + o[i - 1] if s[i] == "(" else o[i - 1]
if s[n - 1] == ")":
    c[n - 1] = 1
for i in range(n - 2, -1, -1):
    c[i] = c[i + 1] + 1 if s[i] == ")" else c[i + 1]
ans = 0
for i in range(n):
    if s[i] == "(":
        a = o[i]
        b = c[i]
        if a != 0 and b != 0:
            ans += fac[a + b - 1] * invfac[a] * invfac[b - 1]
            ans %= m

print(ans)
