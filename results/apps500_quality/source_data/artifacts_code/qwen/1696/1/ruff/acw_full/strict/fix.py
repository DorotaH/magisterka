from sys import stdin


def min_time_to_lighten_city(n, m, k, ignitions):
	# Initialize the grid with False (not on fire)
	grid = [[False] * m for _ in range(n)]

	# Mark the known ignitions as True (on fire)
	for x, y in ignitions:
		grid[x - 1][y - 1] = True

	# Directions for the neighboring blocks (8 possible directions)
	directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	# Initialize the queue with the known ignitions
	queue = ignitions.copy()

	# Initialize the time counter
	time = 0

	# Perform BFS to simulate the spread of fire
	while queue:
		next_queue = []
		for x, y in queue:
			for dx, dy in directions:
				nx, ny = dx + x, dy + y
				if 1 <= nx <= n and 1 <= ny <= m and not grid[nx - 1][ny - 1]:
					grid[nx - 1][ny - 1] = True
					next_queue.append((nx, ny))
		if next_queue:
			time += 1
			queue = next_queue
		else:
			break

	return time


# Read input
n, m, k = map(int, stdin.readline().split())
ignitions = [tuple(map(int, stdin.readline().split())) for _ in range(k)]

# Output the result
print(min_time_to_lighten_city(n, m, k, ignitions))
