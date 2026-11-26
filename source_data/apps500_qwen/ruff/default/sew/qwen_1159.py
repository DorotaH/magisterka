from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, u = heappop(pq)
        if dist[u] < current_dist:
            continue
        for v, weight in graph[u]:
            distance = current_dist + weight
            if dist[v] > distance:
                dist[v] = distance
                heappush(pq, (distance, v))
    return dist


def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m, s = int(data[1]), int(data[2]) - 1

    graph, undirected_edges = defaultdict(list), []

    index = 3
    for _ in range(0, m):
        t = int(data[index])
        u, v = int(data[index + 1]) - 1, int(data[index + 2]) - 1
        index = index + 3

        if t == 1:
            graph[u].append((v, 0))
            graph[v].append((u, 0))
        else:
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            undirected_edges.append((u, v))

    # Plan to maximize the number of reachable vertices
    dist_max = dijkstra(graph, s)
    max_reachable = max(dist_max)
    plan_max = ["-" if dist_max[u] < max_reachable else "+" for u in range(0, n)]

    # Plan to minimize the number of reachable vertices
    dist_min = dijkstra(graph, s)
    min_reachable = min(dist_min)
    plan_min = ["+" if min_reachable < dist_min[u] else "-" for u in range(0, n)]

    # Adjust the plans for undirected edges
    for u, v in undirected_edges:
        if dist_max[v] == dist_max[u] and dist_min[v] == dist_min[u]:
            plan_max[u] = "+"
            plan_max[v] = "+"
            plan_min[u] = "-"
            plan_min[v] = "-"
        elif dist_max[v] < dist_max[u]:
            plan_max[u] = "+"
            plan_max[v] = "-"
            plan_min[u] = "-"
            plan_min[v] = "+"
        elif dist_max[u] < dist_max[v]:
            plan_max[u] = "-"
            plan_max[v] = "+"
            plan_min[u] = "+"
            plan_min[v] = "-"
        elif dist_min[v] < dist_min[u]:
            plan_max[u] = "-"
            plan_max[v] = "+"
            plan_min[u] = "+"
            plan_min[v] = "-"
        else:
            plan_max[u] = "+"
            plan_max[v] = "-"
            plan_min[u] = "-"
            plan_min[v] = "+"

    print(max_reachable)
    print("".join(plan_max))
    print(min_reachable)
    print("".join(plan_min))


solve()
