n = int(input())
m = list(map(int, input().split()))
a = list()
b = []
c = list()
for i in range(0, n):
    if 1 == m[i]:
        a.append(1 + i)
    if 2 == m[i]:
        b.append(1 + i)
    if 3 == m[i]:
        c.append(1 + i)
ans = min(len(a), len(b), len(c))
print(ans)
for i in range(0, ans):
    print(a[i], b[i], c[i])
