import sys

input = sys.stdin.readline


class LCA:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.log = [0] * (1 + n)
        self.lca = [20 * [0] for _ in range(n)]
        self.depth = [0] * (1 + n)

        self.depth[1] = 0
        self.log[1] = 0
        for i in range(2, 1 + n):
            self.log[i] = 1 + self.log[i >> 1]

        stack = [(1, -1, 0)]
        while stack:
            v, p, d = stack.pop()
            self.depth[v] = d
            for u in self.g[v]:
                if u != p:
                    self.lca[u][0] = v
                    stack.append((u, v, 1 + d))
        for j in range(1, self.log[self.n] + 1):
            for i in range(1, 1 + self.n):
                self.lca[i][j] = self.lca[self.lca[i][j - 1]][j - 1]

    def get_lca(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        for i in range(self.log[self.depth[v]] + 1):
            if self.depth[v] - (1 << i) >= self.depth[u]:
                v = self.lca[v][i]
        if u == v:
            return u
        for i in range(self.log[self.depth[v]] + 1):
            if self.lca[u][i] != self.lca[v][i]:
                u = self.lca[u][i]
                v = self.lca[v][i]
        return self.lca[u][0]


def can_connect(u, v):
    if u == v:
        return True
    d = depth[v] - depth[u]
    for i in range(1 + self.log[d]):
        if d >= (1 << i) and self.lca[v][i] in self.g[u]:
            return True
    return False


def solve():
    global g, depth
    n, m = map(int, input().split())
    g = [[] for _ in range(1 + n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    lca = LCA(n, g)
    depth = [0] * (1 + n)
    stack = [(1, -1, 0)]
    while stack:
        v, p, d = stack.pop()
        depth[v] = d
        for u in g[v]:
            if u != p:
                stack.append((u, v, 1 + d))

    for _ in range(m):
        k = int(input())
        v = list(map(int, input().split()))
        if 1 in v:
            ans = "YES"
            for x in v:
                if x != 1 and not can_connect(1, x):
                    ans = "NO"
                    break
        else:
            ans = next(("NO" for x in v if not can_connect(1, x)), "YES")
        print(ans)


if __name__ == "__main__":
    solve()
