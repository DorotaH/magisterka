import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(1, 1, n)

    def build(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.a[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.push(v)
            self.t[v] = max(self.t[2 * v], self.t[2 * v + 1])

    def push(self, v):
        if self.lazy[v]:
            self.t[2 * v] += self.lazy[v]
            self.t[2 * v + 1] += self.lazy[v]
            self.lazy[2 * v] += self.lazy[v]
            self.lazy[2 * v + 1] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, x):
        if l <= tl and tr <= r:
            self.t[v] += x
            self.lazy[v] += x
        else:
            tm = (tl + tr) // 2
            if l <= tm: self.update(2 * v, tl, tm, l, r, x)
            if tm < r: self.update(2 * v + 1, tm + 1, tr, l, r, x)
            self.push(v)
            self.t[v] = max(self.t[2 * v], self.t[2 * v + 1])

    def query(self, v, tl, tr, l, r):
        if l <= tl and tr <= r:
            return self.t[v]
        else:
            tm = (tl + tr) // 2
            self.push(v)
            if r <= tm: return self.query(2 * v, tl, tm, l, r)
            if tm < l: return self.query(2 * v + 1, tm + 1, tr, l, r)
            return max(self.query(2 * v, tl, tm, l, r), self.query(2 * v + 1, tm + 1, tr, l, r))

n = int(input())
a = [0] + list(map(int, input().split()))
q = int(input())

st = SegTree(n)
b = [0] * (n + 1)
c = [0] * (n + 1)
ans = max(a[1], -a[1])
print(a[1])
for l, r, x in (map(int, line.split()) for line in sys.stdin.read().splitlines()):
    st.update(1, 1, n, l, r, x)
    for i in range(l, r + 1):
        b[i] = st.query(1, 1, n, i, i)
        c[i] = a[i] - b[i]
    b_min = b[1]
    c_min = c[1]
    for i in range(2, n + 1):
        b_min = min(b_min, b[i])
        c_min = min(c_min, c[i])
        if b_min + c_min >= a[i]:
            b[i] = b_min
            c[i] = a[i] - b[i]
        else:
            b[i] = a[i] - c_min
            c[i] = c_min
    ans = max(ans, max(b_min, c_min))
    print(ans)
