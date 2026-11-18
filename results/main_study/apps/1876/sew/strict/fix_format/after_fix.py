rr=lambda: input().strip()
rri, rrm = lambda: int(rr()), lambda: list(map(int, rr().split()))
MOD=10**9 + 7

class DSU:
    def __init__(self, N):
        #R * C is the source, and isn't a grid square
        self.par = list(range(N+1))
        self.rnk = [0] * (1+N)
        self.sz = [1] * (1+N)

    def find(self, x):
        if  x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return  self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if  yr == xr: return
        if  self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if  self.rnk[yr] == self.rnk[xr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return  self.sz[self.find(x)]

def solve(N, K, edges):
    graph, dsu = [[] for _ in range(N)], DSU(N)
    for  u,v,w in  edges:
        u=u-1;v=v-1
        if  w==0: #red
            dsu.union(u, v)

    ans=pow(N, K, MOD)
    for  x in  range(0, N):
        if  dsu.find(x)==x:
            ans = ans - pow(dsu.size(x), K, MOD)
            ans = ans % MOD
    return  ans

for  tc in  range(1):#rri()):
    N, K = rrm()
    edges = [rrm() for _ in range(N-1)]
    print(solve(N, K, edges))
