

def  dfs(u, p, p_c, p_h, g):
    for v in g[u]:
        if v != p:
            dfs(v, u, p_c - p_h[u], p_h[u], g)

t = int(input())
for _ in range(0, t):
    n, m = map(int, input().split())
    p, h = list(map(int, input().split())), list(map(int, input().split()))
    g = [[] for  _ in  range(0, n)]
    for  _ in  range(n - 1):
        u, v = map(int, input().split())
        u = u - 1
        v = v - 1
        g[u].append(v)
        g[v].append(u)
    p_c, p_h = sum(p), h[:]
    for  i in  range(n):
        p_c -= p[i]
        p_h[i] += p[i]
    if not dfs(0, -1, p_c, p_h, g) == p_c:
        print('NO')
    else:
        print('YES')
