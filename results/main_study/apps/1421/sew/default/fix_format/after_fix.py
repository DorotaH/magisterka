import sys

input=sys.stdin.readline

oo, n = 10**20, int(input())
a, adj = list(map(int, input().split())), [[] for _ in range(n)]
for  _ in  range(n-1):
    u, v=[int(i)-1 for i in input().split()]
    adj[u].append(v)
    adj[v].append(u)
sm=[0]*n
mx, best = [-oo] * n, [-oo] * n


def  dfs(start):
    stack = [(start, -1)]
    visit = [False] * n
    while stack:
        u, p=stack[-1]
        if visit[u]:
            x = [-oo] * 3
            for v in adj[u]:
                if v != p:
                    sm[u] += sm[v]
                    mx[u] = max(mx[u], mx[v])
                    best[u] = max(best[u], best[v])
                    x[0] = mx[v]
                    x.sort()
            sm[u] += a[u]
            mx[u] = max(mx[u], sm[u])
            if x[1] > -oo and x[2] > -oo:
                cur = x[1] + x[2]
                best[u] = max(best[u], cur)
            stack.pop()
        else:
            for v in adj[u]:
                if v != p:
                    stack.append((v, u))
            visit[u] = True

dfs(0)
ans=max(best)
if ans <= -oo:
    print('Impossible')
else:
    print(ans)
