from collections import defaultdict


class  SegmentTree:
    def  __init__(self, n):
        self.n = n
        self.t = [float('inf')] * (4 * n)
        self.lazy = [0] * (4 * n)
    def  update(self, x, lx, rx, lx2, rx2, v):
        if rx2 < lx or rx < lx2:
            return
        if lx2 <= lx and rx <= rx2:
            self.t[x]=min(self.t[x], v)
            return
        mid = (lx + rx) >> 1
        self.lazy[1 + 2 * x] = min(self.lazy[1 + 2 * x], v)
        self.lazy[2 + 2 * x] = min(self.lazy[2 + 2 * x], v)
        self.push(x)
        self.update(1 + 2 * x, lx, mid, lx2, rx2, v)
        self.update(2 + 2 * x, 1 + mid, rx, lx2, rx2, v)
        self.push(x)
    def  push(self, x):
        self.t[x] += self.lazy[x]
        self.lazy[1 + 2 * x] += self.lazy[x]
        self.lazy[2 + 2 * x] += self.lazy[x]
        self.lazy[x] = 0
    def  query(self, x, lx, rx):
        if rx < self.k:
            return  float('inf')
        if self.k < lx:
            return  float('inf')
        self.push(x)
        if rx == lx:
            return  self.t[x]
        mid = (lx + rx) >> 1
        return  min(self.query(2 * x + 1, lx, mid), self.query(2 * x + 2, mid + 1, rx))

n, q=map(int, input().split())
kindergartens=defaultdict(list)
for i in range(1, 1 + n):
    a, b = map(int, input().split())
    kindergartens[b].append(a)
evenness=200000 * [0]
kindergartens_with_infants = set()
tree = SegmentTree(4 * 200000)
for i in range(1, 1 + n):
    evenness[i] = max(kindergartens[i])
    if  len(kindergartens[i]) > 0:
        tree.update(0, 0, 200000, i, i, evenness[i])
        kindergartens_with_infants.add(i)
for _ in range(q):
    c, d = map(int, input().split())
    tree.update(0, 0, 200_000, c, c, float('inf'))
    tree.update(0, 0, 200_000, d, d, float('inf'))
    if  c in  kindergartens_with_infants:
        kindergartens_with_infants.remove(c)
    if  d in  kindergartens_with_infants:
        kindergartens_with_infants.add(d)
    evenness[1 + _] = tree.query(0, 0, 200_000)
    for i in kindergartens[d]:
        tree.update(0, 0, 200_000, d, d, i)
        if  d in  kindergartens_with_infants:
            tree.update(0, 0, 200_000, d, d, i)
            kindergartens_with_infants.remove(d)
        if  i in  kindergartens_with_infants:
            kindergartens_with_infants.remove(i)
            tree.update(0, 0, 200_000, i, i, i)
    for i in kindergartens[c]:
        tree.update(0, 0, 200_000, c, c, i)
        if  c in  kindergartens_with_infants:
            tree.update(0, 0, 200_000, c, c, i)
            kindergartens_with_infants.remove(c)
        if  i in  kindergartens_with_infants:
            kindergartens_with_infants.remove(i)
            tree.update(0, 0, 200_000, i, i, i)
    for i in kindergartens_with_infants:
        tree.update(0, 0, 200_000, i, i, evenness[i])
print('\n'.join(map(str, evenness[1:1 + q])))
