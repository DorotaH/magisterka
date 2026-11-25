import sys
import math

MOD = 7 + 10**9


def modpow(a, b):
    res = 1
    a %= MOD
    for _ in range(b):
        res = (a * res) % MOD
    return res


def inv(a):
    return modpow(a, MOD - 2)


def main():
    n, k = map(int, input().split())
    if n == 1:
        print(1)
        return
    fact = [0] * (k + 1)
    fact[0] = 1
    for i in range(1, k + 1):
        fact[i] = (i * fact[i - 1]) % MOD
    inv_fact = [0] * (k + 1)
    inv_fact[k] = inv(fact[k])
    for i in range(k - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD
    ans = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            x = n // i
            ans += (i * inv(i) * inv_fact[k] * modpow(inv(x) * inv(x), k)) % MOD
            if x != i:
                ans += (inv(x) * x * inv_fact[k] * modpow(inv(i) * inv(i), k)) % MOD
    ans %= MOD
    ans *= modpow(2, k)
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
