import sys
import bisect

n = int(input())
a = sorted(map(int, input().split()))

ans = 0
max_dist = 0
for i in range(n):
    for j in range(i + 1, n):
        dist = abs(a[j] - a[i])
        if max_dist < dist:
            max_dist = dist
        if a[j] + a[i] <= max_dist and max_dist >= a[i] - a[j]:
            ans += 1

print(ans)
