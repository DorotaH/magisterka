
MOD = 10**9 + 7

def factorial(n):
    f = [1] * (n + 1)
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % MOD
    return f

def ncr(n, r):
    f = factorial(n)
    inv = [0] * (n + 1)
    inv[n] = pow(f[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD
    return (f[n] * inv[r] * inv[n - r]) % MOD

def solve():
    k, s = input().split()
    k, n = int(k), len(s)
    ans = 1
    for c in s:
        ans = (ans * ncr(n + k, k)) % MOD
        n += 1
    return ans

print(solve())
