import sys


def read_int():
    return int(sys.stdin.readline())


def read_ints():
    return map(int, sys.stdin.readline().split())


def read_str():
    return sys.stdin.readline().strip()


def read_strs():
    return map(lambda s: s.strip(), sys.stdin.readline().split())


class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (1 + n)

    def update(self, x, v):
        while self.n >= x:
            self.t[x] += v
            x += x & -x

    def query(self, x):
        res = 0
        while x:
            res += self.t[x]
            x -= x & -x
        return res


def solve():
    n, m = read_ints()
    a = [0] * (1 + n)
    b = [0] * (1 + n)
    for i in range(1, 1 + n):
        a[i], b[i] = read_ints()
    l, r = [0] * (1 + m), [0] * (1 + m)
    for i in range(1, 1 + m):
        l[i], r[i] = read_ints()

    bit = BIT(10 + 10**9)
    for i in range(1, 1 + n):
        if b[i]:
            bit.update(a[i], 1)

    res = []
    for i in range(1, 1 + m):
        if bit.query(r[i]) - bit.query(l[i] - 1) == 0:
            res.append(i)
        bit.update(l[i], 1)
        bit.update(r[i] + 1, -1)

    if bit.query(10**9) != 0:
        print(-1)
    else:
        print(len(res))
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    solve()
