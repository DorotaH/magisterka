import sys

input = sys.stdin.readline

class  LazySegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.t = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, a)

    def build(self, v, tl, tr, a):
        if not tl == tr:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm, a)
            self.build(2 * v + 1, tm + 1, tr, a)
            self.t[v] = self.t[2 * v] + self.t[2 * v + 1]
        else:
            self.t[v] = a[tl]

    def push(self, v):
        if self.lazy[v]:
            tl, tr=self.get_range(v)
            self.t[v]+=self.lazy[v]*(tr-tl+1)
            if  v < self.n:
                self.lazy[2 * v]+=self.lazy[v]
                self.lazy[1 + 2 * v]+=self.lazy[v]
            self.lazy[v]=0

    def get_range(self, v):
        return  self.get_range_idx(v)

    def get_range_idx(self, v):
        if v == 1:
            return 0, self.n - 1
        return  self.get_range_idx(v // 2)

    def update(self, l, r, delta):
        self._update(1, 0, self.n - 1, l, r, delta)

    def _update(self, v, tl, tr, l, r, delta):
        self.push(v)
        if l > tr or tl > r:
            return None
        if tl >= l and r >= tr:
            self.lazy[v]+=delta
            self.push(v)
            return None
        self._update(2 * v, tl, (tl + tr) // 2, l, r, delta)
        self._update(1 + 2 * v, 1 + (tl + tr) // 2, tr, l, r, delta)
        self.t[v] = self.t[2 * v] + self.t[1 + 2 * v]

    def query(self, l, r):
        return  self._query(1, 0, self.n - 1, l, r)

    def _query(self, v, tl, tr, l, r):
        self.push(v)
        if l > tr or tl > r:
            return 0
        if tl >= l and r >= tr:
            return self.t[v]
        return  self._query(v * 2, tl, (tl + tr) // 2, l, r) + self._query(2 * v + 1, (tl + tr) // 2 + 1, tr, l, r)

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
t = [0] * n
for  i in  range(0, n):
    t[i]=a[i]-i
st = LazySegmentTree(t)

ans = 0
for  i in  range(0, n - 1):
    ans+=abs(a[1 + i]-a[i])
print(ans)

for  _ in  range(0, q):
    t_in, x=map(int, input().split())
    if t_in:
        st.update(0, 0, -1, x - 1, x - 1, 1)
    else:
        st.update(0, 0, -1, x - 1, x - 1, -1)
    ans=abs(st.query(0, 0)-st.query(0, 0)-1)+abs(st.query(n-1, n-1)-st.query(n-1, n-1)-1)
    print(ans)
