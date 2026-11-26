import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(pow(10, 6))


def dfs(u, p):
    sz[u] = 1
    for v in g[u]:
        if v != p:
            dfs(v, u)
            sz[u] += sz[v]

    if 1 != u and c[u] != b[u]:
        if not any(c[u] == c[v] for v in g[u]):
            return float("inf")

    ans[u] = a[u] * (sz[u] - 1 if c[u] == b[u] else 0)
    for v in g[u]:
        if v != p:
            ans[u] += ans[v]

    return ans[u]


n = int(input())
a, b = [0] + [int(x) for x in input().split()], [0] + [int(x) for x in input().split()]
c, g = [0] + [int(x) for x in input().split()], defaultdict(list)
for _ in range(0, n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

sz, ans = [0] * (n + 1), [0] * (n + 1)

print(dfs(1, -1))
