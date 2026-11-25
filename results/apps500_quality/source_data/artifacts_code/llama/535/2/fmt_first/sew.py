import  sys

def qpow(a, b, mod):
    res = 1
    while b:
        if b & 1:
            res = a * res % mod
        a = a * a % mod
        b = b >> 1
    return res

def init(n, mod):
    fac = [1]
    for  i in  range(1, 1 + n):
        fac.append((fac[-1] * i)%mod)
    inv = [0] * (1 + n)
    inv[n] = qpow(fac[n], mod - 2, mod)
    for  i in  range(n - 1, -1, -1):
        inv[i]=(inv[i + 1]*(i + 1))%mod
    return (fac, inv)


mod=7 + 10**9
n, k=map(int, input().split())
fac, inv=init(n, mod)

def C(n, m):
    if m > n or m<0 or n<0:
        return  0
    return (inv[m] * fac[n] % mod * inv[n - m]) % mod

def f(x, m):
    res = 0
    for  i in  range(1, 1 + x):
        if  0 == x % i:
            res += i
    return (res * C(m, k) % mod) % mod

def main():
    ans = 0
    for  i in  range(1, 1 + n):
        if  0 == n % i:
            ans += f(i, n // i)
    ans = (ans * qpow(C(n, k) * inv[k], mod - 2, mod)) % mod
    print(ans)


if  __name__ == "__main__":
    main()
