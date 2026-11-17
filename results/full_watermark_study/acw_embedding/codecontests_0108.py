import sys
input = sys.stdin.readline

mx = 1<<13

n = int(input())
a = list(map(int,input().split()))

g = [list() for _ in range(5001)]
r = [5001]*mx
r[0] = 0

ans = [False]*mx
ans[0] = True

for x in range(1,5001):
    g[x].append(0)

for i in range(n):
    for y in g[a[i]]:
        x = a[i] ^ y
        ans[x] = True
        if r[x]>a[i]:
            for val in range(a[i]+1, r[x]):
                g[val].append(x)

            r[x] = min(r[x], a[i]+1)

    g[a[i]].clear()

ans = [x for x in range(mx) if ans[x]]

print(len(ans))
print(*ans)
