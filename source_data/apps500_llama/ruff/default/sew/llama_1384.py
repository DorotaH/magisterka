import sys
import math
import heapq

N, INF = int(2e5 + 10), int(1e18)


class SegTree:
    def __init__(self, n):
        self.n = n
        self.t = [[-INF, -INF] for _ in range(4 * n)]

    def upd(self, p, val):
        self.update(0, 0, self.n - 1, p, val)

    def update(self, k, tl, tr, p, val):
        if tl == tr:
            self.t[k] = [val, val]
        else:
            tm = (tl + tr) // 2
            if p <= tm:
                self.update(2 * k + 1, tl, tm, p, val)
            else:
                self.update(2 * k + 2, tm + 1, tr, p, val)
            self.t[k] = max(self.t[2 * k + 1], self.t[2 * k + 2])

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, k, tl, tr, l, r):
        if l > r or l > tr or tl > r:
            return [-INF, -INF]
        if tl >= l and r >= tr:
            return self.t[k]
        tm = (tl + tr) // 2
        return max(
            self._query(2 * k + 1, tl, tm, l, r),
            self._query(2 * k + 2, tm + 1, tr, l, r),
        )


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    tree = SegTree(n)
    for i in range(n):
        tree.upd(i, a[i])
    for _ in range(m):
        k, pos = map(int, input().split())
        s = 0
        for i in range(pos - 1, n):
            p = tree.query(i, i).max
            if p == -INF:
                break
            s = s + p
            if s >= k:
                print(p)
                break
            if i == n - 1:
                print(a[i])
                break


solve()
