import sys

input = sys.stdin.readline

mod = 998244353
N = 5 + 10**5


def add(x, y):
    return (y + x) % mod


def mul(x, y):
    return (y * x) % mod


def pow(x, y):
    if y == 0:
        return 1
    z = pow(x, y // 2)
    return mul(z, z) if y % 2 == 0 else mul(x, mul(z, z))


def inv(x):
    return pow(x, mod - 2)


class Comb:
    def __init__(self, n):
        self.fac = [1] * (1 + n)
        self.invfac = [0] * (1 + n)
        self.inv = [0] * (1 + n)
        for i in range(1, 1 + n):
            self.fac[i] = mul(self.fac[i - 1], i)
        self.invfac[n] = inv(self.fac[n])
        for i in range(n, 0, -1):
            self.invfac[i - 1] = mul(self.invfac[i], i)
            self.inv[i] = mul(self.invfac[i], self.fac[i - 1])

    def fac(self, n):
        return self.fac[n]

    def invfac(self, n):
        return self.invfac[n]

    def inv(self, n):
        return self.inv[n]

    def C(self, n, m):
        if m > n or m < 0 or 0 > n:
            return 0
        return mul(self.fac[n], mul(self.invfac[m], self.invfac[n - m]))


comb = Comb(N)

n, k, len_ = map(int, input().split())
a = list(map(int, input().split()))

pref = [0] * (1 + n)
for i in range(n):
    pref[i + 1] = pref[i] if a[i] == -1 else pref[i] + 1
cnt = [0] * (k + 1)
for i in range(n - len_ + 1):
    if a[i] == -1:
        cnt[0] += 1

for i in range(len_ - 1):
    cnt[a[len_ + i] - 1] += 1

ans = 0
for i in range(1, k + 1):
    cur = pow(k - i + 1, len_ - 1)
    for j in range(i + 1):
        cur = mul(cur, comb.C(cnt[j], 1))
    ans = add(ans, cur)

print(ans)
