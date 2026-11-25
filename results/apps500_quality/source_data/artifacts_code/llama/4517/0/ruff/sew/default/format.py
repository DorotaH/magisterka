from collections import deque, defaultdict
import sys

input = sys.stdin.readline


class LCA:
    def __init__(self, n):
        self.n = n
        self.log = 0
        self.log2 = 0
        while (1 << self.log) <= n:
            self.log += 1
        self.log2 = self.log
        while (1 << self.log2) < n:
            self.log2 += 1

    def build(self, tree):
        self.log = 0
        self.log2 = 0
        while (1 << self.log) <= self.n:
            self.log += 1
        self.log2 = self.log
        while (1 << self.log2) < self.n:
            self.log2 += 1
        self.n = len(tree)
        self.depth = [-1] * self.n
        self.parent = [[-1] * self.log2 for _ in range(self.n)]
        self.root = 0
        self.depth[self.root] = 0
        stack = [(self.root, -1)]
        for i in range(0, self.log2):
            for v in stack:
                p = v[0]
                par = v[1]
                self.parent[p][i] = self.parent[par][i] if i > 0 else -1
                if self.parent[p][i] == -1:
                    self.depth[p] = self.depth[par] + 1
                stack.append((self.parent[p][i], p))
        self.log = self.log2

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for i in range(0, self.log):
            if (self.depth[v] - self.depth[u]) >> i & 1:
                v = self.parent[v][i]
        if v == u:
            return u
        for i in reversed(range(self.log)):
            if self.parent[v][i] != self.parent[u][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]
        return self.parent[u][0]

    def dist(self, u, v):
        return self.depth[u] - self.depth[v]


class Tree:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(self.n)]
        self.query = [[] for _ in range(self.n)]
        self.query_count = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def add_query(self, k, v):
        self.query_count += 1
        self.query[self.query_count] = [v[:], k]

    def dfs(self, v, p, lca, tree):
        self.visited = [0] * self.n
        self.depth = [0] * self.n
        self.depth[v] = 0
        self.visited[v] = 1
        stack = [v]
        while stack:
            v = stack.pop()
            for u in self.adj[v]:
                if u != p and not self.visited[u]:
                    self.depth[u] = self.depth[v] + 1
                    self.visited[u] = 1
                    stack.append(u)
                    lca.add(self.depth[u], self.depth[v])
                    for i in range(self.query_count, 0, -1):
                        for u2 in self.query[i][0]:
                            if self.depth[u2] < self.depth[v]:
                                lca.add(self.depth[u], self.depth[u2])

    def solve(self):
        lca.build(self.adj)
        self.dfs(0, -1, lca, self)


n, m = map(int, input().split())
tree = Tree(n)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree.add_edge(u - 1, v - 1)
for _ in range(m):
    k = list(map(int, input().split()))[0]
    tree.add_query(k, list(map(lambda x: x - 1, input().split()[1:])))

tree.solve()
for _ in range(m):
    if tree.query[_ + 1][1]:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
