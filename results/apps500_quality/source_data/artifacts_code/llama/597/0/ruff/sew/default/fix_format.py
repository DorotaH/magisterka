import heapq
import sys


def dijkstra(graph, start):
    distances = {city: float("inf") for city in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_city = heapq.heappop(queue)
        if distances[current_city] < current_distance:
            continue
        for neighbor in graph[current_city]:
            distance = 1 + current_distance
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = {city: list() for city in range(1, n + 1)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    attacked_cities, min_distance = list(map(int, input().split())), float("inf")
    for start in attacked_cities:
        distances = dijkstra(graph, start)
        distance = sum(distances[city] for city in attacked_cities)
        if distance < min_distance:
            min_distance, teleport_city = distance, start
    print(teleport_city)
    print(min_distance)


if __name__ == "__main__":
    main()
