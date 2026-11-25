from collections import deque
from heapq import heappop, heappush


def min_time_to_cross(n, m, d, g, r):
	# Add safety islands at the start and end of the road
	d = sorted(d) + [0] + [n]
	m += 2

	# Initialize the time taken to reach each position
	time = [float('inf')] * (1 + n)
	time[0] = 0

	# Initialize the queue for BFS
	queue = deque([(0, 0)])  # (position, direction, time)

	while queue:
		pos, dir, t = queue.popleft()

		# If we have reached the end of the road, return the time
		if pos == n:
			return t

		# Calculate the next positions
		next_pos = pos + dir
		next_t = t + 1

		# If we can move to the next position and it is within the bounds
		if 0 <= next_pos <= n and next_t >= g + time[pos] and next_t < time[next_pos]:
			time[next_pos] = next_t
			queue.append((next_pos, dir, next_t))

		# If we are on a safety island, we can change direction
		if pos in d:
			for new_dir in [-1, 1]:
				if new_dir != dir:
					next_t = t + 1
					if g + time[pos] <= next_t:
						time[pos] = next_t
						queue.append((pos, new_dir, next_t))

	# If we cannot cross the road, return -1
	return -1


# Read input
n, m = map(int, input().split())
d = list(map(int, input().split()))
g, r = map(int, input().split())

# Output the result
print(min_time_to_cross(n, m, d, g, r))
