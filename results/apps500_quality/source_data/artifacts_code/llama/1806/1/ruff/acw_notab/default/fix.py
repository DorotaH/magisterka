

class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.x = x


class SegTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.A = [Node(0) for _ in range(2 * self.N - 1)]

    def build(self, nodes, l, r, x):
        self.A[x].x = 0
        if l == r:
            self.A[x].x = 1
            return
        mid = (l + r) // 2
        self.build(nodes, l, mid, 2 * x + 1)
        self.build(nodes, mid + 1, r, 2 * x + 2)
        self.A[x].x = max(self.A[2 * x + 1].x, self.A[2 * x + 2].x)

    def update(self, l, r, x, i, v):
        if l == r:
            self.A[x].x = v
            return
        mid = (l + r) // 2
        if i <= mid:
            self.update(l, mid, 2 * x + 1, i, v)
        else:
            self.update(mid + 1, r, 2 * x + 2, i, v)
        self.A[x].x = max(self.A[2 * x + 1].x, self.A[2 * x + 2].x)

    def query(self, l, r, x, ql, qr):
        if l >= ql and qr >= r:
            return self.A[x].x
        if r < ql or qr < l:
            return 0
        mid = (l + r) // 2
        return max(self.query(l, mid, 2 * x + 1, ql, qr), self.query(mid + 1, r, 2 * x + 2, ql, qr))


n, m = map(int, input().split())
nodes = []
for _ in range(n):
    l, r = map(int, input().split())
    nodes.append((l, r))

nodes.sort(key=lambda x: x[1])

t = SegTree(n)
t.build(nodes, 0, n - 1, 0)

for _ in range(m):
    x, y = map(int, input().split())
    it = 0
    while it < n and nodes[it][0] < x:
        it += 1
    ans = -1
    if it == n:
        print(-1)
        continue
    if nodes[it][0] > x:
        ans = 1
    while it < n and nodes[it][1] <= y:
        if nodes[it][0] <= x:
            ans = max(ans, t.query(0, n - 1, 0, nodes[it][0], nodes[it][1]))
        it += 1
    if ans == -1:
        print(-1)
    else:
        print(ans)
