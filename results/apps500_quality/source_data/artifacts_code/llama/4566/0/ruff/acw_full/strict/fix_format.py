from collections import defaultdict


def count_roads(n, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, 1 + n):
        print(len(graph[i]))


n, m = map(int, input().split())
roads = []
for _ in range(m):
    u, v = map(int, input().split())
    roads.append((u, v))

count_roads(n, roads)
