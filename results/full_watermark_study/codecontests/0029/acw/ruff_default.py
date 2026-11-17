import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = 998244353

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    g = [[] for i in range(n)]
    for i in range(n - 1):
        x, y = map(int, input().split())
        g[x - 1] += [y - 1]
        g[y - 1] += [x - 1]
    f = [0] * n
    parent = [0] * n
    f[1] = pow(2, n - 1, MOD)
    order = [0]
    for v in order:
        for u in g[v]:
            if u != parent[v]:
                parent[u] = v
                order += [u]

    def dfs(k):
        size = [0] * n
        for v in reversed(order):
            if size[v] % k == 0:
                if v != 0:
                    size[parent[v]] += 1
            elif v == 0 or (1 + size[v]) % k != 0:
                return False
        return True

    for i in range(2, n):
        if (n - 1) % i == 0:
            f[i] = int(dfs(i))
    h = [0] * (1 + n)
    for i in range(n - 1, 0, -1):
        h[i] = f[i]
        for j in range(i * 2, n, i):
            h[i] -= h[j]
    print(*(x for x in h[1 : 1 + n]))
