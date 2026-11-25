import sys

input=sys.stdin.readline


class  Tree:
    def  __init__(self, n, edges, primes, powers):
        self.n=n
        self.edges=edges
        self.primes=primes
        self.powers=powers
        self.factorization={}
        self.parent=[-1]*(n + 1)
        self.depth=[0]*(n + 1)
        self.n1=0
        self.n2=0
        self.res=0

    def  dfs(self, u, p):
        self.parent[u]=p
        for  v in  self.edges[u]:
            if p != v:
                self.depth[v] = self.depth[u] + 1
                self.dfs(v, u)
        self.dfs1(u)

    def  dfs1(self, u, p=None):
        if p is not None:
            self.n1+=self.powers[self.primes.index(self.primes[u])][0]
            self.n2+=self.powers[self.primes.index(self.primes[u])][1]
        for  v in  self.edges[u]:
            if p != v:
                self.dfs1(v, u)

    def  power(self, x, y):
        res=1
        while  y:
            if  y % 2 == 1:
                res *= x
                res %= 1000000007
            x *= x
            x %= 1000000007
            y //= 2
        return res

    def  solve(self):
        self.dfs(1)
        for  i in  range(self.n2):
            self.n2-=1
            self.n1+=1
        self.n1%=1_000_000_007
        for  i in  range(self.n2):
            self.n2-=1
            self.n1-=1
        self.n1%=1_000_000_007
        self.n2%=1_000_000_007
        self.res=self.power(2, self.n1)*self.n2
        self.res%=1_000_000_007
        for  p in  self.primes:
            if p != 2:
                self.res = self.res * self.power(p, self.powers[self.primes.index(p)][1])
                self.res %= 1_000_000_007
        for  i in  range(1, self.n):
            for  j in  range(i + 1, self.n):
                self.res=(self.res+((self.depth[i] + self.depth[j]) * (self.n - self.depth[i] - self.depth[j])))%1000000007
        print(self.res)

t=int(input())
for _ in range(0, t):
    n=int(input())
    edges=[list() for  _ in  range(n + 1)]
    for _ in range(0, n - 1):
        u, v=map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    m, primes = int(input()), list(map(int, input().split()))
    powers=list()
    for p in primes:
        power1 = power2 = 0
        while  p % 2 == 0:
            p //= 2
            power2 += 1
        power1=n-power2
        powers.append([power1, power2])
    tree=Tree(n, edges, primes, powers)
    tree.solve()
