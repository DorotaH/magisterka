import sys
import math


def floyd(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = 0 if i == j else graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[k][j] + dist[i][k])

    return max(max(row) for row in dist)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(floyd(graph))
