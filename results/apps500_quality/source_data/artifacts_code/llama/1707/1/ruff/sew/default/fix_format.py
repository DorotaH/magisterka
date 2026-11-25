n = int(input())
a = sorted(list(map(int, input().split())))

ans = max_dist = 0
for i in range(n):
    for j in range(1 + i, n):
        dist = abs(a[j] - a[i])
        max_dist = max(max_dist, dist)
        if a[i] + a[j] <= max_dist and a[i] - a[j] <= max_dist:
            ans += 1

print(ans)
