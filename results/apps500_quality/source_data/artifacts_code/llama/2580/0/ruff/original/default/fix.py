import sys

input = sys.stdin.readline

def dfs(v, p, graph, depth, n):
    depth[v] = 0
    for u in graph[v]:
        if u != p:
            depth[v] = max(depth[v], 1 + dfs(u, v, graph, depth, n))

def solve():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    depth = [0] * n
    dfs(0, -1, graph, depth, n)

    p = list(map(int, input().split()))
    d = {}
    for x in p:
        d[x] = d.get(x, 0) + 1

    ans = 0
    for p, c in d.items():
        ans = (ans + (n - 2) * c) % (10 ** 9 + 7)
        for i in range(2, n - 1):
            ans = (ans - c * (i - 1) * (n - 2 - i + 1) * (n - 2) % (10 ** 9 + 7)) % (10 ** 9 + 7)
        for i in range(1, n):
            ans = (ans + c * (n - 2) * depth[i] * (n - 1 - depth[i]) % (10 ** 9 + 7)) % (10 ** 9 + 7)

    print(ans)

t = int(input())
for _ in range(t):
    solve()
