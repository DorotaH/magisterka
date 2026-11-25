import sys

n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    d[i+1] = a[i]

e = []
for _ in range(s):
    l, r = map(int, input().split())
    e.append((l, r))

e.sort(key=lambda x: x[1])

ans = -1

for mask in range(1 << s):
    sum = 0
    count = 0
    b = d.copy()
    for i in range(s):
        l, r = e[i]
        if (mask >> i) & 1:
            for j in range(l, r+1):
                b[j] = -1
            count += r - l + 1
            if r - l + 1 >= k:
                sum = max(sum, a[r-1])
            if r - l + 1 > k:
                break

    if count == m and sum >= a[k-1]:
        ans = max(ans, a[min(count, n)])

print(ans)
