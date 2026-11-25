import sys

input = sys.stdin.readline


class SegTree:
    def __init__(self, n, func, default=0, depth=20):
        self.n = n
        self.func = func
        self.default = default
        self.depth = depth
        self.tree = [[self.default] * (2**i + 1) for i in range(depth)]

    def _build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = [self.default, self.default]
        else:
            tm = (tl + tr) >> 1
            self._build(2 * v, tl, tm)
            self._build(2 * v + 1, tm + 1, tr)
            self.tree[v][0] = self.func(self.tree[2 * v][0], self.tree[2 * v + 1][0])
            self.tree[v][1] = self.func(self.tree[2 * v][1], self.tree[2 * v + 1][1])

    def _update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = [new_val, new_val]
        else:
            tm = (tl + tr) >> 1
            if pos <= tm:
                self._update(2 * v, tl, tm, pos, new_val)
            else:
                self._update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v][0] = self.func(self.tree[2 * v][0], self.tree[2 * v + 1][0])
            self.tree[v][1] = self.func(self.tree[2 * v][1], self.tree[2 * v + 1][1])

    def _query(self, v, tl, tr, l, r):
        if l > r:
            return self.default, self.default
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) >> 1
        return self.func(
            self._query(2 * v, tl, tm, l, min(r, tm)),
            self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r),
        )

    def build(self):
        self._build(1, 0, self.n - 1)

    def update(self, pos, new_val):
        self._update(1, 0, self.n - 1, pos, new_val)

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    queries = []
    for _ in range(m):
        k, pos = map(int, input().split())
        queries.append((k, pos))

    segtree = SegTree(n, lambda x, y: x if x[0] > y[0] else y, (0, 0))
    segtree.build()

    for i in range(n):
        segtree.update(i, (a[i], a[i]))

    for k in range(n, 0, -1):
        s = 0
        for i in range(n):
            s += a[i]

        prev_max = 0
        for i in range(k):
            left, right = i, n - 1
            while left <= right:
                mid = (left + right) >> 1
                x, y = segtree.query(i, mid)
                if s - y >= x:
                    prev_max = x
                    right = mid - 1
                else:
                    left = mid + 1

        for i in range(n):
            if segtree.query(i, i)[0] == prev_max:
                print(a[i])
                break
        segtree.update(i, (0, 0))


for _ in range(1):
    solve()
