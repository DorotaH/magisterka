import sys

def qpow(a, b, mod):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def init(n, mod):
    fac = [1]
    for i in range(1, n + 1):
        fac.append((fac[-1] * i) % mod)
    inv = [0] * (n + 1)
    inv[n] = qpow(fac[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod
    return fac, inv

mod = 10 ** 9 + 7
n, k = map(int, input().split())
fac, inv = init(n, mod)

def C(n, m):
    if m > n or m < 0 or n < 0:
        return 0
    return (fac[n] * inv[m] % mod * inv[n - m]) % mod

def f(x, m):
    res = 0
    for i in range(1, x + 1):
        if x % i == 0:
            res += i
    return (res * C(m, k) % mod) % mod

def main():
    ans = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ans += f(i, n // i)
    ans = (ans * qpow(C(n, k) * inv[k], mod - 2, mod)) % mod
    print(ans)

if __name__ == "__main__":
    main()
