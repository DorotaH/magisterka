import math


class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.lazy = [0] * (4 * self.n)
        self.data = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, data)

    def build(self, v, tl, tr, a):
        if tl == tr:
            self.data[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm, a)
            self.build(2 * v + 1, tm + 1, tr, a)
            self.data[v] = max(self.data[2 * v], self.data[2 * v + 1])

    def push(self, v, tl, tr):
        if self.lazy[v]:
            self.data[v] += self.lazy[v]
            if tl != tr:
                self.lazy[2 * v] += self.lazy[v]
                self.lazy[2 * v + 1] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, inc):
        self.push(v, tl, tr)
        if l > r:
            return
        if l == tl and tr == r:
            self.data[v] += inc
            self.lazy[v] += inc
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), inc)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, inc)
            self.data[v] = max(self.data[2 * v], self.data[2 * v + 1])

    def query(self, v, tl, tr, l, r):
        self.push(v, tl, tr)
        if l > r:
            return -math.inf
        if l == tl and tr == r:
            return self.data[v]
        else:
            tm = (tl + tr) // 2
            return max(self.query(2 * v, tl, tm, l, min(r, tm)),
                      self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))

def check(l, r, a):
    if l == r:
        return 'Yes'
    mx1 = LazySegmentTree(a)
    mx2 = LazySegmentTree(a)
    mx1.update(1, 0, len(a) - 1, l - 1, r - 1, 0)
    mx2.update(1, 0, len(a) - 1, l - 1, r - 1, 0)
    mx1.update(1, 0, len(a) - 1, l, r - 1, 1)
    mx2.update(1, 0, len(a) - 1, l, r - 1, -1)
    mx = mx1.query(1, 0, len(a) - 1, l - 1, r - 1)
    mm = mx2.query(1, 0, len(a) - 1, l - 1, r - 1)
    if mx == mm:
        return 'Yes'
    else:
        return 'No'

n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    print(check(l, r, a))
