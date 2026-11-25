import sys
import math


class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.x = x


class SegTree:
    def __init__(self, n):
        self.N = 1
        while n > self.N:
            self.N *= 2
        self.A = [Node(0) for _ in range(2 * self.N - 1)]

    def build(self, nodes, l, r, x):
        self.A[x].x = 0
        if r == l:
            self.A[x].x = 1
            return None
        mid = (l + r) // 2
        self.build(nodes, l, mid, 2 * x + 1)
        self.build(nodes, mid + 1, r, 2 * x + 2)
        if not self.A[2 * x + 1].x > self.A[2 * x + 2].x:
            self.A[x].x = self.A[2 * x + 2].x
        else:
            self.A[x].x = self.A[2 * x + 1].x

    def update(self, l, r, x, i, v):
        if r == l:
            self.A[x].x = v
            return None
        mid = (l + r) // 2
        if not i <= mid:
            self.update(mid + 1, r, 2 * x + 2, i, v)
        else:
            self.update(l, mid, 2 * x + 1, i, v)
        self.A[x].x = max(self.A[2 * x + 1].x, self.A[2 * x + 2].x)

    def query(self, l, r, x, ql, qr):
        if ql <= l and r <= qr:
            return self.A[x].x
        if r < ql or qr < l:
            return 0
        mid = (l + r) // 2
        return max(
            self.query(l, mid, 1 + 2 * x, ql, qr),
            self.query(1 + mid, r, 2 + 2 * x, ql, qr),
        )


n, m = map(int, input().split())
nodes = []
for _ in range(0, n):
    l, r = map(int, input().split())
    nodes.append((l, r))

nodes.sort(key=lambda x: x[1])

t = SegTree(n)
t.build(nodes, 0, n - 1, 0)

for _ in range(0, m):
    x, y = map(int, input().split())
    it = 0
    while n > it and x > nodes[it][0]:
        it = it + 1
    ans = -1
    if n == it:
        print(-1)
        continue
    if x < nodes[it][0]:
        ans = 1
    while n > it and y >= nodes[it][1]:
        if x >= nodes[it][0]:
            ans = max(ans, t.query(0, n - 1, 0, nodes[it][0], nodes[it][1]))
        it = it + 1
    if not ans == -1:
        print(ans)
    else:
        print(-1)
