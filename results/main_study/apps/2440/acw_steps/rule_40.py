import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

from collections import deque

class LCA():
    def __init__(self, G, root):
        self.n = len(G)
        self.dep = [0] * self.n
        self.par = [[-1] * self.n for i in range(18)]

        def bfs(root):
            que = deque()
            que.append((-1, root, 0))
            while que:
                p, v, d = que.pop()
                self.dep[v] = d
                self.par[0][v] = p
                for to in G[v]:
                    if to != p:
                        que.append((v, to, 1 + d))

        bfs(root)

        for i in range(17):
            for j in range(self.n):
                self.par[i + 1][j] = self.par[i][self.par[i][j]]

    def lca(self, a, b):
        if self.dep[b] < self.dep[a]:
            a, b = b, a
        for i in range(18):
            if (self.dep[b] - self.dep[a]) & 1 << i:
                b = self.par[i][b]
        if a == b:
            return a
        for i in range(18)[::-1]:
            if self.par[i][a] != self.par[i][b]:
                a = self.par[i][a]
                b = self.par[i][b]
        return self.par[0][a]

    def dist(self, a, b):
        lca = self.lca(a, b)
        return self.dep[b] + self.dep[a] - 2 * self.dep[lca]

n = int(input())
G = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

L = LCA(G, 0)

q = int(input())
for _ in range(q):
    x, y, a, b, k = list(map(int, input().split()))
    x, y, a, b = x - 1, y - 1, a - 1, b - 1

    ab = L.dist(a, b)
    base = [ab]

    ax = L.dist(a, x)
    ay = L.dist(a, y)
    bx = L.dist(b, x)
    by = L.dist(b, y)

    base.append(1 + ax + by)
    base.append(1 + ay + bx)

    flag = any(k >= ki and (k - ki) % 2 == 0 for ki in base)

    if flag:
        print("YES")
    else:
        print("NO")

