
n = int(input())
a = list(map(int, input().split()))

max_coolness = [0] * (1 + n)
max_coolness[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    max_coolness[i] = max(a[i], max_coolness[i + 1])

ans = [-1] * n
for i in range(n):
    if max_coolness[0] <= a[i]:
        ans[i] = n
        continue
    j = i
    c = 1
    while True:
        j = (1 + j) % n
        c += 1
        if a[j] < (1 + max_coolness[i]) // 2:
            break
        if j == i:
            ans[i] = c
            break

print(*ans)
