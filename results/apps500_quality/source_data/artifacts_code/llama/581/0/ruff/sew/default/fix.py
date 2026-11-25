import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(u, p, e, fa):
    L[u] = 0
    for  v in  G[u]:
        if p != v:
            dfs(v, u, e, fa)
            L[u]=max(L[u], L[v]+e[v])


def dfs2(u, p, fa):
    for  v in  G[u]:
        if p != v:
            dfs2(v, u, fa)
            P[u]=max(P[u], P[v]+e[v])

n = int(input())
G = defaultdict(list)
e = [0] * (n + 1)
P = [0] * (n + 1)
L = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    e[a] += 1
    e[b] += 1

dfs(1, 0, e, L)
P[1] = L[1]
dfs2(1, 0, fa=0)
ans = 0
for i in range(2, n + 1):
    ans += P[i]
    ans -= L[i]
print(ans)

for i in range(2, n + 1):
    m = max(L[i], P[i])
    print(i, G[i][0], m, file=sys.stderr)
    G[m].remove(i)
    G[i].remove(m)
    e[i] -= 1
    e[m] -= 1
