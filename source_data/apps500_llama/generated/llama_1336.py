from math import inf

n = int(input())
a = list(map(int, input().split()))

max_coolness = [0] * (n + 1)
max_coolness[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    max_coolness[i] = max(a[i], max_coolness[i + 1])

ans = [-1] * n
for i in range(n):
    if a[i] >= max_coolness[0]:
        ans[i] = n
        continue
    j = i
    c = 1
    while True:
        j = (j + 1) % n
        c += 1
        if a[j] < (max_coolness[i] + 1) // 2:
            break
        if j == i:
            ans[i] = c
            break

print(*ans)
