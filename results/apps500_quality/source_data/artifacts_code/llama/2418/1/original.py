import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [[a[i] + i for i in range(n)] for _ in range(4)]
        self.lazy = [0] * (4 * n)

    def propagate(self, node):
        if self.lazy[node]:
            self.tree[node] = [v + self.lazy[node] for v in self.tree[node]]
            if node < 2:
                self.lazy[node << 1] += self.lazy[node]
                self.lazy[(node << 1) + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l, r, node, L, R, i):
        if l <= L and R <= r:
            self.lazy[node] += r - L + 1
            self.tree[node][0] += r - L + 1
            if node < 2:
                self.lazy[node << 1] += r - L + 1
                self.lazy[(node << 1) + 1] += r - L + 1
        else:
            self.propagate(node)
            mid = (L + R) >> 1
            if l <= mid:
                self.update(l, r, node << 1, L, mid, i)
            if r > mid:
                self.update(l, r, (node << 1) + 1, mid + 1, R, i)

    def query(self, l, r, node, L, R):
        if l <= L and R <= r:
            self.propagate(node)
            if l == r:
                return self.tree[node][l]
            return max(self.tree[node][l], self.tree[node][r])
        mid = (L + R) >> 1
        if r <= mid:
            return self.query(l, r, node << 1, L, mid)
        if l > mid:
            return self.query(l, r, (node << 1) + 1, mid + 1, R)
        return max(self.query(l, r, node << 1, L, mid), self.query(l, r, (node << 1) + 1, mid + 1, R))

n = int(input())
a = list(map(int, input().split()))
q = int(input())
a = [0] + a
for _ in range(q):
    l, r, x = map(int, input().split())
    a[l] += x
    a[r + 1] -= x

b = [0] * (n + 1)
c = [0] * (n + 1)
st_b = SegmentTree(n, b)
st_c = SegmentTree(n, c)

ans = float('-inf')
for i in range(1, n + 1):
    st_b.update(i, i, 1, 1, n, i - 1)
    st_c.update(i, i, 2, 1, n, i - 1)
    ans = max(st_b.query(i, i, 1, 1, n), st_c.query(i, i, 2, 1, n))
print(ans)

for _ in range(q):
    st_b.update(1, n, 1, 1, n, 0)
    st_c.update(1, n, 2, 1, n, 0)
    for i in range(1, n + 1):
        st_b.update(i, i, 1, 1, n, -1)
        st_c.update(i, i, 2, 1, n, 1)
    for i in range(1, n + 1):
        st_b.update(i, i, 1, 1, n, a[i])
        st_c.update(i, i, 2, 1, n, -a[i])
    ans = float('-inf')
    for i in range(1, n + 1):
        ans = max(st_b.query(i, i, 1, 1, n), st_c.query(i, i, 2, 1, n))
    print(ans)
