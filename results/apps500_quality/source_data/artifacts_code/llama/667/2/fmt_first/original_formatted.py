import sys
import math


def floyd(graph):
    n = len(graph)
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return max(max(row) for row in dist)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(floyd(graph))
