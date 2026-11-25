import sys

input = sys.stdin.readline

n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
a = [-a[i] for i in range(n)]
b = [list() for _ in range(n + 1)]
for _ in range(0, s):
    l, r=map(int, input().split())
    b[l-1].append(r)

f = [0] * (n + 1)
for i in range(0, n):
    for  x in  b[i]:
        f[x] += 1

g = [0] * (n + 1)
for i in range(1, n + 1):
    g[i]=g[i-1]+f[i]

ans = -1
for l in range(1, n + 1):
    if g[r - 1] - g[l - 1] >= k:
        c=[0]*(n + 1)
        for i in range(l, r):
            c[i] = 1
        for i in range(l, r):
            for x in b[i]:
                c[x]+=1
        for i in range(l, r):
            for x in b[i]:
                c[x]=0

        p=[0]*(n + 1)
        for i in range(1, 1 + n):
            p[i] = p[i - 1] + c[i]
        v=[0]*(n + 1)
        for i in range(1, 1 + n):
            v[p[i]] = a[i - 1]

        if k <= p[r - 1]:
            ans = a[l - 1]
        else:
            ans = -1

        break

print(-1 if ans == -1 else -ans)
