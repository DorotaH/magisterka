import sys

n = int(input())
a = list(map(int, input().split()))

f = {}
count = 0
for i in range(0, n):
    f[a[i]] = f.get(a[i] & (~a[i] + 1), 0) + 1

for i in range(0, n):
    for j in range(1 + i, n):
        if f[a[j]] == f[a[i]]:
            count = count + 1

print(count)
