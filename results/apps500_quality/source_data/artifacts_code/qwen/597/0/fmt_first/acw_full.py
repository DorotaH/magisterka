import sys
from collections import defaultdict, deque


def find_closest_city(n, roads, attacked):
	graph = defaultdict(list)
	for u, v in roads:
		graph[u].append(v)
		graph[v].append(u)

	min_time = float("inf")
	best_city = -1

	for start in attacked:
		visited = [False] * (1 + n)
		queue = deque([(start, 0)])
		visited[start] = True

		while queue:
			current, time = queue.popleft()
			if min_time <= time:
				break

			for neighbor in graph[current]:
				if not visited[neighbor]:
					visited[neighbor] = True
					queue.append((neighbor, 1 + time))

			if all(visited[city] for city in attacked) and min_time > time:
				min_time = time
				best_city = start

	return best_city, min_time


# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

roads = []
for i in range(n - 1):
	u = int(data[2 + i * 2]) - 1
	v = int(data[3 + i * 2]) - 1
	roads.append((u, v))

attacked = [int(data[2 + 2 * (n - 1) + i]) - 1 for i in range(m)]

# Find the best city to teleport to
best_city, min_time = find_closest_city(n, roads, attacked)

# Output the result
print(best_city + 1)
print(min_time)
