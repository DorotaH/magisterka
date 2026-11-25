from sys import stdin

n=int(stdin.readline())
a, G = list(map(int, stdin.readline().split())), [[] for _ in range(n)]
for _ in range(0, n - 1):
    u, v = map(int, stdin.readline().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

visited, stack = [False] * n, [0]
while stack:
    u=stack.pop()
    visited[u]=True
    for  v in  G[u]:
        if  not  visited[v]:
            stack.append(v)

color_u, color_v = a[:], a[:]
for u in range(0, n):
    for  v in  G[u]:
        if  2 == a[u]:
            color_v[v]=2
        elif  2 == a[v]:
            color_u[v] = 2

ans=0
for u in range(0, n):
    for  v in  G[u]:
        if  (1 == color_u[u] or  1 == color_v[v]) and  (1 == color_u[v] or  1 == color_v[u]):
            continue
        ans += 1

print(ans)