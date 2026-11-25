import sys

input = sys.stdin.readline

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

MOD = 998244353

def power(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        x = power(a, p // 2)
        return x * x % MOD
    else:
        x = power(a, p - 1)
        return a * x % MOD

def ncr(n, r):
    return (fact[n] * invfact[r] % MOD * invfact[n - r]) % MOD

def fact(n):
    factlist = [1]
    for i in range(1, n + 1):
        factlist.append((factlist[i - 1] * i) % MOD)
    return factlist

def invfact(n):
    invfactlist = [0] * (n + 1)
    invfactlist[n] = power(fact[n], MOD - 2)
    for i in range(n - 1, -1, -1):
        invfactlist[i] = (invfactlist[i + 1] * (i + 1)) % MOD
    return invfactlist

n, k = read_ints()
factlist = fact(n * 2)
invfactlist = invfact(n * 2)

ans = 0
for m in range(1, n + 1):
    if m * m >= k:
        break
    for i in range(n - m + 1):
        if m % 2 == 1 and (n - m) % 2 == 1:
            continue
        for col in range(1, n - (n - m) + 1):
            if (m % 2 == 1 and col % 2 == 1) or (m % 2 == 0 and col % 2 == 0):
                continue
            ans = (ans + ncr(n, m) * ncr(n, col) * factlist[n * 2 - m - col] * invfactlist[n - m] % MOD * invfactlist[n - col]) % MOD

print(ans)
