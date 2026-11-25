
n = int(input())
a = list(map(int, input().split()))

f = {}
count = 0
for i in range(n):
    f[a[i]] = f.get(a[i] & (1 + ~a[i]), 0) + 1

for i in range(n):
    for j in range(i + 1, n):
        if f[a[i]] == f[a[j]]:
            count += 1

print(count)
