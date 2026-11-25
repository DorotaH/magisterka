import  sys
import  math


class LazySegmentTree:
    def  __init__(self, data):
        self.n=len(data)
        self.lazy=[0]*(self.n * 4)
        self.data=[0]*(self.n * 4)
        self.build(1, 0, self.n-1, data)

    def  build(self, v, tl, tr, a):
        if not tl == tr:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm, a)
            self.build(2 * v + 1, tm + 1, tr, a)
            self.data[v] = max(self.data[2 * v], self.data[2 * v + 1])
        else:
            self.data[v] = a[tl]

    def  push(self, v, tl, tr):
        if  self.lazy[v]:
            self.data[v]+=self.lazy[v]
            if  tr != tl:
                self.lazy[v * 2] += self.lazy[v]
                self.lazy[2 * v + 1] += self.lazy[v]
            self.lazy[v]=0

    def  update(self, v, tl, tr, l, r, inc):
        self.push(v, tl, tr)
        if  r < l:
            return
        if not (l == tl and tr == r):
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), inc)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, inc)
            self.data[v] = max(self.data[2 * v], self.data[2 * v + 1])
        else:
            self.data[v] += inc
            self.lazy[v] += inc

    def  query(self, v, tl, tr, l, r):
        self.push(v, tl, tr)
        if  r < l:
            return -math.inf
        if not (l == tl and tr == r):
            tm = (tl + tr) // 2
            return max(self.query(2 * v, tl, tm, l, min(r, tm)),
                      self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))
        else:
            return self.data[v]


def check(l, r, a):
    if r == l:
        return 'Yes'
    mx1, mx2 = LazySegmentTree(a), LazySegmentTree(a)
    mx1.update(1, 0, len(a) - 1, l - 1, r - 1, 0)
    mx2.update(1, 0, len(a) - 1, l - 1, r - 1, 0)
    mx1.update(1, 0, len(a) - 1, l, r - 1, 1)
    mx2.update(1, 0, len(a) - 1, l, r - 1, -1)
    mx, mm = mx1.query(1, 0, len(a) - 1, l - 1, r - 1), mx2.query(1, 0, len(a) - 1, l - 1, r - 1)
    if not mx == mm:
        return 'No'
    else:
        return 'Yes'

n, m = map(int, input().split())
a = list(map(int, input().split()))
for  _ in  range(0, m):
    l, r = map(int, input().split())
    print(check(l, r, a))