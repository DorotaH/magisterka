n = int(input())
a = list(map(int, input().split()))

min_dist = float('inf')

for i in range(0, n):
    for  j in  range(1 + i, n):
        dist=abs(a[0]-a[i])+abs(a[-1]-a[j])+sum([abs(a[k] - a[k - 1]) for k in range(1, j)])
        min_dist=min(min_dist, dist)

print(min_dist)
