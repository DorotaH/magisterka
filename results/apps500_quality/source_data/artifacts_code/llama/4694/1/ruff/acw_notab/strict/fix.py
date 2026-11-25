n = int(input())
a = list(map(int, input().split()))

min_dist = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        dist = (
            abs(a[-1] - a[j])
            + abs(a[0] - a[i])
            + sum(abs(a[k] - a[k - 1]) for k in range(1, j))
        )
        min_dist = min(min_dist, dist)

print(min_dist)
