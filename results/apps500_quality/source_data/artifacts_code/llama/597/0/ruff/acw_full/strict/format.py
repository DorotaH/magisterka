from collections import deque
import sys
import heapq


def dijkstra(graph, start):
    distances = {city: float("inf") for city in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_city = heapq.heappop(queue)
        if current_distance > distances[current_city]:
            continue
        for neighbor in graph[current_city]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = {city: [] for city in range(1, 1 + n)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    attacked_cities = list(map(int, input().split()))
    min_distance = float("inf")
    for start in attacked_cities:
        distances = dijkstra(graph, start)
        distance = sum(distances[city] for city in attacked_cities)
        if min_distance > distance:
            min_distance = distance
            teleport_city = start
    print(teleport_city)
    print(min_distance)


if __name__ == "__main__":
    main()
