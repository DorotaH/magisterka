import sys
import math

input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, p, value):
        self._update(p, value, 0, 0, self.n - 1)

    def _update(self, p, value, node, start, end):
        if start == end:
            self.tree[node] = min(self.tree[node] + value, value)
        else:
            mid = (start + end) // 2
            if p <= mid:
                self._update(p, value, 2 * node + 1, start, mid)
            else:
                self._update(p, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, l, r):
        return self._query(l, r, 0, 0, self.n - 1)

    def _query(self, l, r, node, start, end):
        if l > end or r < start:
            return 0
        if l <= start and r >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self._query(l, r, 2 * node + 1, start, mid), self._query(l, r, 2 * node + 2, mid + 1, end))

def solve():
    n, k, a, b, q = map(int, input().split())
    tree = SegmentTree(n)

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            d, a = map(int, query[1:])
            tree.update(d - 1, a)
        else:
            p = int(query[1])
            filled = 0
            for i in range(p - 1, n):
                if i + k > n:
                    break
                filled += min(a * (i + k - p) + b * (n - i - k), tree.query(i + 1, min(i + k - 1, n - 1)))
                if i + k >= p:
                    break
            print(filled)

if __name__ == '__main__':
    solve()
