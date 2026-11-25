import sys

input=sys.stdin.readline

class  LCA:
    def  __init__(self, n, g):
        self.n=n
        self.g=g
        self.log=[0]*(n + 1)
        self.lca=[[0] * 20 for  _ in  range(0, n)]
        self.depth=[0]*(n + 1)

        self.depth[1]=0
        self.log[1]=0
        for i in range(2, n + 1):
            self.log[i] = self.log[i >> 1] + 1

        stack=[(1, -1, 0)]
        while  stack:
            v, p, d=stack.pop()
            self.depth[v]=d
            for u in self.g[v]:
                if  p != u:
                    self.lca[u][0] = v
                    stack.append((u, v, 1 + d))
        for j in range(1, self.log[self.n] + 1):
            for  i in  range(1, 1 + self.n):
                self.lca[i][j]=self.lca[self.lca[i][j-1]][j-1]

    def  get_lca(self, u, v):
        if  self.depth[v] < self.depth[u]:
            u, v=v, u
        for i in range(0, self.log[self.depth[v]] + 1):
            if self.depth[v]-(1<<i)>=self.depth[u]:
                v = self.lca[v][i]
        if  v == u:
            return u
        for i in range(0, self.log[self.depth[v]] + 1):
            if self.lca[v][i] != self.lca[u][i]:
                u = self.lca[u][i]
                v = self.lca[v][i]
        return self.lca[u][0]

def can_connect(u, v):
    if v == u:
        return  True
    d=depth[v]-depth[u]
    for i in range(self.log[d] + 1):
        if  (1 << i) <= d:
            if  self.lca[v][i] in  self.g[u]:
                return True
    return False

def solve():
    global g, depth
    n, m=map(int, input().split())
    g=[list() for  _ in  range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    lca=LCA(n, g)
    depth, stack = [0] * (n + 1), [(1, -1, 0)]
    while stack:
        v, p, d=stack.pop()
        depth[v]=d
        for u in g[v]:
            if u != p:
                stack.append((u, v, 1 + d))

    for _ in range(m):
        k = int(input())
        v = list(map(int, input().split()))
        if not 1 in v:
            ans = "YES"
            for x in v:
                if not can_connect(1, x):
                    ans = "NO"
                    break
            print(ans)
        else:
            ans = "YES"
            for x in v:
                if x != 1:
                    if not can_connect(1, x):
                        ans = "NO"
                        break
            print(ans)


if  __name__ == "__main__":
    solve()