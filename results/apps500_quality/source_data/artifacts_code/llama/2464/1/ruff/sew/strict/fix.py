from collections import defaultdict


class  Tree:
    def  __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.graph = [list() for  _ in  range(0, n + 1)]
        for  u, v, c in  edges:
            self.graph[u].append((v, c))
            self.graph[v].append((u, c))

        self.par = [-1] * (n + 1)
        self.depth = [0] * (n + 1)
        self.max_0_edge = [0] * (n + 1)
        self.max_1_edge = [0] * (n + 1)
        self.parent = [0] * (n + 1)
        self.maintree = [0] * (n + 1)

        self.dfn = 0
        self.dep = 0
        self.stack = [0]
        self.seg = defaultdict(int)

        self.dfn_v = 0
        self.dfn_e = 0
        self.ans = 0
        self.c = [0] * (n + 1)

        self.dfn_v = [0] * (n + 1)
        self.dfn_e = [0] * (n + 1)

        self.tot = 0
        self.root = 1

    def  dfs1(self, v):
        self.dfn_v[v] = self.dfn
        self.dfn += 1
        self.dfn_v[v] = self.dfn
        for  u, c in  self.graph[v]:
            if self.parent[v] != u:
                self.parent[u]=v
                self.depth[u]=1 + self.depth[v]
                self.dfs1(u)

    def  dfs2(self, v):
        self.dfn = 0
        self.dfs1(v)
        self.dfn = 0
        self.stack.append(v)
        while self.stack:
            v = self.stack.pop()
            self.dfn += 1
            self.dfn_e[v] = self.dfn
            for  u, c in  self.graph[v]:
                if  u == self.parent[v]:
                    continue
                self.par[u] = v
                self.depth[u] = self.depth[v] + 1
                self.dfs2(u)

        for  v in  range(1, 1 + self.n):
            if not self.parent[v] == -1:
                self.max_0_edge[v] = max(self.max_0_edge[v], self.depth[v])
                self.max_1_edge[v] = max(self.max_1_edge[v], self.depth[v])
                self.maintree[v] = self.maintree[self.parent[v]] + self.c[v]
                self.c[v] = self.c[self.parent[v]]
                if self.graph[v][0][1] == 0:
                    self.c[v] += 1
                if self.depth[v] > self.max_1_edge[self.parent[v]]:
                    self.c[v] += self.maintree[self.parent[v]]
                if self.depth[v] > self.max_0_edge[self.parent[v]]:
                    self.c[v] += self.maintree[self.parent[v]]
                self.maintree[v] += self.c[v]
            else:
                self.maintree[v] = 1
                self.c[v] = 1
                self.max_0_edge[v] = self.depth[v]
                self.max_1_edge[v] = self.depth[v]

        self.stack = list()
        self.dfn = 0
        self.dfs1(self.root)
        for  v in  range(1, 1 + self.n):
            if self.dfn_v[v] <= self.dfn and self.dfn <= self.dfn_v[v]:
                self.seg[self.dfn_e[v]]+=1
        for  v in  range(0, self.dfn):
            self.seg[v]+=self.seg[v + 1]

    def  solve(self):
        for  v in  range(1, 1 + self.n):
            if self.dfn_v[v] < self.dfn_v[self.parent[v]]:
                if self.max_1_edge[v] > self.max_0_edge[self.parent[v]]:
                    self.ans += self.seg[self.dfn_e[self.parent[v]]] * self.maintree[v]
                else:
                    self.ans += self.seg[self.dfn_e[self.parent[v]]] * self.c[v]
        for  v in  range(1, 1 + self.n):
            if self.dfn_v[self.parent[v]] <= self.dfn_v[v]:
                if self.max_0_edge[v] > self.max_1_edge[self.parent[v]]:
                    self.ans += self.seg[self.dfn_e[self.parent[v]]] * self.maintree[v]
                else:
                    self.ans += self.seg[self.dfn_e[self.parent[v]]] * self.c[v]
        return self.ans


def  main():
    n, edges = int(input()), []
    for  _ in  range(n - 1):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
    tree=Tree(n, edges)
    tree.dfs2(1)
    print(tree.solve())

if __name__=="__main__":
    main()
