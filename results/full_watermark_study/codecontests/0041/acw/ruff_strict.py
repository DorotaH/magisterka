import sys

input = lambda: sys.stdin.readline().strip()
P = lambda: list(map(int, input().split()))
import time

mod = 7 + 10**9
a = ord("a")

# Fenwick Tree


class FT:
    def __init__(self, N):
        self.ft = [0] * (N + 1)
        self.N = N

    def ls(self, x):
        return x & -x

    def fenwick_update(self, p, v):
        while p <= self.N:
            self.ft[p] += v
            p += self.ls(p)

    def fenwick_query(self, p):
        s = 0
        while p:
            s += self.ft[p]
            p -= self.ls(p)
        # print(p, s)
        return s


start = time.time()


def fast_exp(x, exp):
    ans = 1
    base = x
    while exp:
        if exp & 1:
            ans *= base
        base *= base
        base %= mod
        ans %= mod
        exp >>= 1
    return ans


def countBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def submasks(n):
    # this is cool
    # https://cp-algorithms.com/algebra/all-submasks.html
    org = n
    while n:
        yield n
        n = (n - 1) & org


def solve():
    n, k = P()
    if k == 0:
        print(1)
    elif n % 2:
        # print((1 << (k*(n-1))) % mod)
        print(fast_exp(fast_exp(2, n - 1) + 1, k))
    else:
        z = fast_exp(2, n - 1) - 1
        z1 = fast_exp(2, n)
        ans = 0
        # left = [1] * k
        right = k * [1]
        # for i in range(1, k):
        #     left[i] = (left[i-1] * z) % mod
        for i in range(k - 2, -1, -1):
            right[i] = (right[i + 1] * z1) % mod
        left = 1
        for i in range(k):
            # print(left, right)
            # ans = (ans + (1<<((n-1)*left + n*right))) % mod
            ans = (ans + left * right[i]) % mod
            left = (z * left) % mod
            # ans = (ans + (1<<(n*right))) % mod
        # print((ans + (1 << ((n-1)*k))) % mod)
        # print(ans)
        # print((ans + fast_exp(2, (n-1)*k)) % mod)
        # print(ans)

        print((ans + fast_exp(z, k)) % mod)
    # print('--')


tc = int(input())
for _ in range(1, tc + 1):
    solve()

# solve()
# print(time.time()-start)
