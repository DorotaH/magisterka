import  sys
import  heapq

def read_input():
    n, m=map(int, input().split())
    graph=[list() for  _ in  range(0, n + 1)]
    for  _ in  range(n - 1):
        u, v=map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    attacked_cities=list(map(int, input().split()))
    return n, m, graph, attacked_cities

def bfs(graph, start):
    distance = [float('inf')] * (n + 1)
    queue = [(0, start)]
    distance[start]=0
    while  queue:
        d, u=heapq.heappop(queue)
        for v in graph[u]:
            if distance[v] > 1 + d:
                distance[v] = d + 1
                heapq.heappush(queue, (distance[v], v))
    return distance

def main():
    global  n
    global  attacked_cities
    n, m, graph, attacked_cities=read_input()
    distance_from_start=bfs(graph, 1)
    distance_from_attacked_cities = {city: distance_from_start[city] for city in attacked_cities}
    min_distance = float('inf')
    teleport_city=None
    for  city in  distance_from_attacked_cities:
        distance=distance_from_start[1]+distance_from_attacked_cities[city]
        if distance < min_distance:
            min_distance, teleport_city = distance, city
    print(teleport_city)
    print(min_distance)

if  __name__ == "__main__":
    main()
