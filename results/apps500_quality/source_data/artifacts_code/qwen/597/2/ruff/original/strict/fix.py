import sys
from heapq import heappop, heappush


def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heappop(pq)
        if current_dist > dist[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heappush(pq, (distance, neighbor))
    return dist

def find_best_teleport(n, m, roads, attacked_cities):
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append((v-1, 1))
        graph[v-1].append((u-1, 1))

    min_time = float('inf')
    best_city = -1

    for city in range(n):
        dist = dijkstra(graph, city)
        total_time = sum(dist[city-1] for city in attacked_cities)
        if total_time < min_time:
            min_time = total_time
            best_city = city + 1

    return best_city, min_time

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    roads = []
    for _ in range(n - 1):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        roads.append((u, v))
        index += 2

    attacked_cities = [int(data[index + i]) for i in range(m)]

    best_city, min_time = find_best_teleport(n, m, roads, attacked_cities)

    print(best_city)
    print(min_time)

if __name__ == "__main__":
    main()
