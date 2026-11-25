import sys

class SegmentTree:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tree = [0] * (4 * n)
        self.cuts = [0] * (4 * n)
    def update(self, node, l, r, i, x):
        if not l == r:
            m = (l + r) // 2
            if i <= m:
                self.update(2 * node, l, m, i, x)
            else:
                self.update(2 * node + 1, m + 1, r, i, x)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        else:
            self.tree[node] = x
    def query(self, node, l, r, ql, qr):
        if  l == ql and  qr == r:
            return  self.tree[node]
        m = (l + r) // 2
        if  m >= qr:
            return  self.query(2 * node, l, m, ql, qr)
        elif  m < ql:
            return  self.query(1 + 2 * node, 1 + m, r, ql, qr)
        else:
            return  self.query(node * 2, l, m, ql, m) + self.query(2 * node + 1, m + 1, r, m + 1, qr)
    def add_cut(self, node, l, r, i, j):
        if not l == r:
            m = (l + r) // 2
            if j <= m:
                self.add_cut(2 * node, l, m, i, j)
            else:
                self.add_cut(2 * node + 1, m + 1, r, i, j)
            self.cuts[node] = self.cuts[2 * node] ^ self.cuts[2 * node + 1]
        else:
            self.cuts[node] ^= 1
    def get_cuts(self):
        return  [i for  i in  range(1, self.m + 1) if  self.cuts[i]]

def  main():
    input=sys.stdin.readline
    n, m=map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for  i in  range(1, 1 + n):
        a[i], b[i] = map(int, input().split())
    cords=list()
    for  i in  range(1, 1 + m):
        cords.append(tuple(map(int, input().split())))

    cords.sort(key=lambda x: x[0])
    segment_tree=SegmentTree(n, m)
    for  i in  range(1, 1 + n):
        segment_tree.update(1, 1, n, a[i], b[i])

    cuts=list()
    for  i in  range(1, 1 + m):
        segment_tree.add_cut(1, 1, n, cords[i - 1][0], cords[i - 1][1])
        if  segment_tree.query(1, 1, n, 1, n) == 0:
            cuts.append(i)

    if segment_tree.query(1, 1, n, 1, n) != 0:
        print(-1)
    else:
        print(len(cuts))
        print(' '.join(map(str, cuts)))

if  __name__=="__main__":
    main()