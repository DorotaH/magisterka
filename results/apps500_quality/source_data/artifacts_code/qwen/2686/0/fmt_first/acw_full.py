import sys
from collections import deque


def bfs_shortest_path(N, M, close_buildings, S, T):
	# Create an adjacency list for the graph
	adj_list = [[] for _ in range(N + 1)]
	for A, B in close_buildings:
		adj_list[A].append(B)
		adj_list[B].append(A)

	# Initialize the visited array and the queue for BFS
	visited = [False] * (N + 1)
	queue = deque([(S, 0)])  # (current building, current jumps)

	# Perform BFS
	while queue:
		current, jumps = queue.popleft()
		if current == T:
			return jumps
		if visited[current]:
			continue
		visited[current] = True
		for neighbor in adj_list[current]:
			if not visited[neighbor]:
				queue.append((neighbor, jumps + 1))

	# If the queue is exhausted and we haven't reached the target, return 0
	return 0


# Read input
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
close_buildings = [
	(int(data[2 + i * 2]) - 1, int(data[3 + i * 2]) - 1) for i in range(M)
]
S = int(data[2 + 2 * M]) - 1
T = int(data[3 + 2 * M]) - 1

# Find the shortest path
result = bfs_shortest_path(N, M, close_buildings, S, T)

# Print the result
print(result)
