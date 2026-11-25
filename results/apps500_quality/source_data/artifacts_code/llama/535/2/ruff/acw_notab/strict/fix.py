

def qpow(a, b, mod):
    res = 1
    while b:
        if b & 1:
            res = a * res % mod
        a = a * a % mod
        b >>= 1
    return res


def init(n, mod):
    fac = [1]
    fac.extend((i * fac[-1]) % mod for i in range(1, 1 + n))
    inv = [0] * (1 + n)
    inv[n] = qpow(fac[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod
    return fac, inv


mod = 7 + 10 ** 9
n, k = map(int, input().split())
fac, inv = init(n, mod)


def C(n, m):
    if m > n or m < 0 or n < 0:
        return 0
    return (inv[m] * fac[n] % mod * inv[n - m]) % mod


def f(x, m):
    res = sum(i for i in range(1, 1 + x) if x % i == 0)
    return (C(m, k) * res % mod) % mod


def main():
    ans = sum(f(i, n // i) for i in range(1, 1 + n) if n % i == 0)
    ans = (ans * qpow(C(n, k) * inv[k], mod - 2, mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
