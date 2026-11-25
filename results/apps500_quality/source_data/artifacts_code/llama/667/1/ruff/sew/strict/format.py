import sys
import math

n, inf = int(input()), sys.maxsize
dist, edges = (
    [[inf] * n for _ in range(n)],
    [[float(x) for x in input().split()] for _ in range(n)],
)

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(0, n):
        for j in range(0, n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(max(max(row) for row in dist))
