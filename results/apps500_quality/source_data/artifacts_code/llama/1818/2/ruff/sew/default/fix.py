n = int(input())
a = list(map(int, input().split()))

f = dict()
for  x in  a:
    f[x]=f.get(x//2, f.get(x-1, 0))+(x % 2 == 1)

ans = 0
for  i in  range(n):
    for j in range(1 + i, n):
        if f[a[j]] == f[a[i]]:
            ans = ans + 1

print(ans)
