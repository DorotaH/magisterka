n = int(input())
m = list(map(int, input().split()))
a = list()
b = []
c = list()
for i in range(0, n):
    if  m[i] == 1:
        a.append(1 + i)
    if  m[i] == 2:
        b.append(1 + i)
    if  m[i] == 3:
        c.append(1 + i)
ans = min(len(a), len(b), len(c))
print(ans)
for i in range(0, ans):
    print(a[i], b[i], c[i])
