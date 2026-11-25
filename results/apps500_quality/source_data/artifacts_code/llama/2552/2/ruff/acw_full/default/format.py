import sys
from collections import deque


def dfs(u, p, p_c, p_h, g):
    for v in g[u]:
        if v != p:
            dfs(v, u, p_c - p_h[u], p_h[u], g)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    h = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    p_c = sum(p)
    p_h = h[:]
    for i in range(n):
        p_c -= p[i]
        p_h[i] += p[i]
    if dfs(0, -1, p_c, p_h, g) == p_c:
        print("YES")
    else:
        print("NO")
