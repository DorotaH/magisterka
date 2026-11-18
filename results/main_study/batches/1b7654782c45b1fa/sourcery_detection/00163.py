k, n = map(int, input().split())
points = list(map(int, input().split()))

dist = []
for i in range(n):
    if i != n-1:
        distance = points[i+1] - points[i]
    else:
        distance = points[0]+k - points[i]
    dist.append(distance)

max = dist[0]
for j in range(1, len(dist), 1):
    max = max(max, dist[j])
dist.remove(max)

ans = sum(k for k in dist)
print(ans)