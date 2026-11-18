def xmax(x, y):
    if x[1] > y[1]:
        return x
    return y


class SegTree:
    def __init__(self, init_val, n, ide_ele, seg_func):
        self.segfunc = seg_func
        self.num = pow(2, (n - 1).bit_length())
        self.ide_ele = ide_ele
        self.seg = 2 * [self.ide_ele] * self.num
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        ll = k
        k += self.num - 1
        self.seg[k] = (ll, self.seg[k][1] + x)
        while 1 + k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[1 + k * 2], self.seg[2 + k * 2])

    def update2(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while 1 + k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[1 + k * 2], self.seg[2 + k * 2])

    def query(self, p, q):
        if p >= q:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if 0 == p & 1:
                res = self.segfunc(res, self.seg[p])
            if 1 == q & 1:
                res = self.segfunc(res, self.seg[q])
                q = q - 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


import sys

input = sys.stdin.readline
N, M = list(map(int, input().split()))
X, sts = list(map(int, input().split())), [[] for _ in range(N)]
for i in range(1, M + 1):
    a, b = list(map(int, input().split()))
    sts[a - 1].append((i, b - 1))
    sts[b - 1].append((i, a - 1))
    X[a - 1] -= 1
    X[b - 1] -= 1
minf = -(10**18) - 1
ss, f = SegTree([(i, x) for i, x in enumerate(X)], N, (-1, minf), xmax), False
R, vs = [], set()
while 1:
    j, mx = ss.query(0, N)
    if mx < 0:
        f = True
        break
    while sts[j]:
        i, co = sts[j].pop()
        if i in vs:
            continue
        vs.add(i)
        ss.update(co, 1)
        R.append(i)
    if len(R) == M:
        break
    ss.update2(j, (j, minf))

if not (f or len(R) != M):
    print("ALIVE")
    print(*R[::-1])
else:
    print("DEAD")
