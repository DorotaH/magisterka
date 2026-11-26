import sys


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n * 4)

    def update(self, i, val):
        self._update(i, val, 0, 0, self.n - 1)

    def _update(self, i, val, node, start, end):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if i <= mid:
                self._update(i, val, 2 * node + 1, start, mid)
            else:
                self._update(i, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, start, end):
        return self._query(start, end, 0, 0, self.n - 1)

    def _query(self, start, end, node, n_start, n_end):
        if end < n_start or n_end < start:
            return 0
        if start <= n_start and n_end <= end:
            return self.tree[node]
        mid = (n_start + n_end) // 2
        return self._query(start, end, 1 + 2 * node, n_start, mid) + self._query(
            start, end, 2 + 2 * node, 1 + mid, n_end
        )


n, tree = int(input()), SegmentTree(100000)
for _ in range(0, n):
    l, r = map(int, input().split())
    tree.update(l - 1, 1)
    tree.update(r, -1)

print(tree.query(0, 99999))
