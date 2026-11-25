import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(10**6)

def dfs(u, p):
    sz[u] = 1
    for v in g[u]:
        if v != p:
            dfs(v, u)
            sz[u] += sz[v]

    if u != 1 and b[u] != c[u]:
        if not any(c[v] == c[u] for v in g[u]):
            return float('inf')

    ans[u] = a[u] * (sz[u] - 1 if b[u] == c[u] else 0)
    for v in g[u]:
        if v != p:
            ans[u] += ans[v]

    return ans[u]

n = int(input())
a = [0] + [int(x) for x in input().split()]
b = [0] + [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
g = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

sz = [0] * (n + 1)
ans = [0] * (n + 1)

print(dfs(1, -1))
