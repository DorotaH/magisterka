import sys
import math

n = int(input())
inf = sys.maxsize
dist = [[inf] * n for _ in range(n)]
edges = [[float(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(max(max(row) for row in dist))
