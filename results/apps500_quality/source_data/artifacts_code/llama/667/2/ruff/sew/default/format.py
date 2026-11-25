import sys
import math


def floyd(graph):
    n = len(graph)
    dist = []
    for _ in range(n):
        dist.append([float("inf")] * n)
    for i in range(0, n):
        for j in range(n):
            if not i == j:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = 0

    for k in range(0, n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return max(max(row) for row in dist)


n = int(input())
graph = []
for _ in range(0, n):
    graph.append(list(map(int, input().split())))

print(floyd(graph))
