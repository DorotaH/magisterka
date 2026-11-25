def can_survive(n, m, w, friends):
	from collections import defaultdict
	from heapq import heappush, heappop

	# Create adjacency list for the graph
	graph = defaultdict(list)
	for i, (x, y) in enumerate(friends, start=1):
		graph[x].append((y, i))
		graph[y].append((x, i))

	# Initialize priority queue with friends who can be called immediately
	pq = []
	for i in range(1, 1 + n):
		if len(graph[i]) == 1:
			heappush(pq, (1, i))

	# Initialize visited set to keep track of friends who have been called
	visited = set()

	# Process the priority queue
	while pq:
		count, friend = heappop(pq)
		if friend in visited:
			continue
		visited.add(friend)
		for neighbor, id in graph[friend]:
			if id not in visited:
				heappush(pq, (count + 1, neighbor))

	# Check if all friends have been called
	return (True, list(visited)) if len(visited) == m else (False, None)


# Read input
n, m = map(int, input().split())
w = list(map(int, input().split()))
friends = [tuple(map(int, input().split())) for _ in range(m)]

# Determine if Lee can survive and get the order
survive, order = can_survive(n, m, w, friends)

# Output the result
if survive:
	print("ALIVE")
	print(*order)
else:
	print("DEAD")
