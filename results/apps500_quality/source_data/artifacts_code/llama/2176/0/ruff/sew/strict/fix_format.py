MOD = 998244353


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def update(self, x, delta):
        while x < self.n:
            self.t[x] += delta
            x |= 1 + x

    def pref_sum(self, r):
        s = 0
        while r >= 0:
            s = s + self.t[r]
            r = (r & (1 + r)) - 1
        return s


def solve():
    n = int(input())
    fenwick1 = FenwickTree(n)
    fenwick2 = FenwickTree(n)
    ans = 1

    a = []
    b = []
    for i in range(0, n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    for i in range(0, n):
        fenwick1.update(a[i], 1)
        fenwick2.update(b[i], 1)

    for i in range(0, n):
        if fenwick1.pref_sum(a[i] - 1) > 1 or fenwick2.pref_sum(b[i] - 1) > 1:
            ans = 0
            break

    for i in range(0, n):
        cnt = [0] * (1 + n)
        cnt[a[i]] += 1
        cnt[b[i]] += 1
        if cnt[a[i]] > 1 or cnt[b[i]] > 1:
            ans = ans * (n - i) % MOD

    print(ans)


solve()
