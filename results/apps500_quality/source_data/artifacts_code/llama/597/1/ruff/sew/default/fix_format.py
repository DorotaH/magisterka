from collections import deque


def dijkstra(graph, start):
    queue, visited = deque([(start, 0)]), {start}
    distances = {start: 0}

    while queue:
        city, dist = queue.popleft()
        for neighbor in graph[city]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)
                distances[neighbor] = dist + 1

    return distances


def main():
    n, m = map(int, input().split())
    graph = [list() for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    attacked_cities = list(map(int, input().split()))

    min_distance, teleportation_point = float("inf"), None

    for city in attacked_cities:
        distances = dijkstra(graph, city)
        distance = sum(distances[city] for city in attacked_cities)
        distance = distance - 1  # subtract 1 for teleportation

        if distance < min_distance:
            min_distance, teleportation_point = distance, city

    print(teleportation_point)
    print(min_distance)


if __name__ == "__main__":
    main()
