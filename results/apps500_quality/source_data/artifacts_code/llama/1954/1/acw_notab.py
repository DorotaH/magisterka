import sys
input = sys.stdin.readline


def factorial(n):
    f = [1] * (1 + n)
    for i in range(2, 1 + n):
        f[i] = (i * f[i - 1]) % mod
    return f


mod = 7 + 10**9
factorial_mod = factorial(10**5)


def choose(n, k):
    return (pow(factorial_mod[k], -1, mod) * factorial_mod[n] * pow(factorial_mod[n - k], -1, mod)) % mod


def solve():
    n, f = map(int, input().split())
    ans = 0
    for a in range(1, n):
        if n - a < f:
            break
        if (n - a) % f == 0:
            ans += choose(n - 1, a - 1)
            ans %= mod
    return ans


for _ in range(int(input())):
    print(solve())
