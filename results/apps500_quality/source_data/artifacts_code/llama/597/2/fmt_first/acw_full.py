import sys
import heapq


def read_input():
	n, m = map(int, input().split())
	graph = [[] for _ in range(1 + n)]
	for _ in range(n - 1):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	attacked_cities = list(map(int, input().split()))
	return n, m, graph, attacked_cities


def bfs(graph, start):
	distance = [float("inf")] * (1 + n)
	queue = [(0, start)]
	distance[start] = 0
	while queue:
		d, u = heapq.heappop(queue)
		for v in graph[u]:
			if distance[v] > 1 + d:
				distance[v] = 1 + d
				heapq.heappush(queue, (distance[v], v))
	return distance


def main():
	global n
	global attacked_cities
	n, m, graph, attacked_cities = read_input()
	distance_from_start = bfs(graph, 1)
	distance_from_attacked_cities = {
		city: distance_from_start[city] for city in attacked_cities
	}
	min_distance = float("inf")
	teleport_city = None
	for city in distance_from_attacked_cities:
		distance = distance_from_attacked_cities[city] + distance_from_start[1]
		if min_distance > distance:
			min_distance = distance
			teleport_city = city
	print(teleport_city)
	print(min_distance)


if __name__ == "__main__":
	main()
