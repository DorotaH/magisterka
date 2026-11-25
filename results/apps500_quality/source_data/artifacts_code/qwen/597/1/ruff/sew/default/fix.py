import sys
from collections import defaultdict, deque


def find_closest_city(n, roads, attacked_cities):
    # Build the graph
    graph=defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    # Function to perform BFS and find the minimum distance from a source to any attacked city
    def bfs(start):
        visited, queue = [False] * (n + 1), deque([(start, 0)])
        visited[start]=True
        while queue:
            current, distance = queue.popleft()
            if current in attacked_cities:
                return  distance
            for  neighbor in  graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))
        return  float('inf')
    
    # Find the city that minimizes the maximum distance to any attacked city
    min_distance, optimal_city = float('inf'), float('inf')
    for city in range(1, n + 1):
        distance = bfs(city)
        if min_distance > distance:
            min_distance, optimal_city = distance, city
    
    return optimal_city, min_distance

# Read input
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
roads = []
for i in range(n - 1):
    u, v = int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1
    roads.append((u, v))
attacked_cities = list(map(int, data[2 * n + 1:2 * n + 1 + m])) - 1

# Find the optimal city and the minimum time
optimal_city, min_time = find_closest_city(n, roads, attacked_cities)

# Output the result
print(optimal_city + 1)
print(min_time)