import sys
from collections import deque


def min_time_to_cross(n, d, g, r):
	# Convert d to a set for O(1) lookups
	d = set(d)
	# Initialize the queue with the starting position and time
	queue = deque([(0, 0)])
	# Initialize the visited set to keep track of visited positions and times
	visited = set()
	visited.add((0, 0))
	
	while queue:
		pos, time = queue.popleft()
		# Check if we have reached the end of the road
		if pos == n:
			return time
		
		# Calculate the time until the next green light
		next_green_time = (time // (g + r) + 1) * (g + r) + g
		
		# Move to the right if possible and within the green light
		if pos + 1 <= n and next_green_time >= 1 + time:
			new_time = 1 + time
			if (pos + 1, new_time) not in visited:
				visited.add((pos + 1, new_time))
				queue.append((pos + 1, new_time))
		
		# Move to the left if possible and within the green light
		if pos - 1 >= 0 and next_green_time >= 1 + time:
			new_time = 1 + time
			if (pos - 1, new_time) not in visited:
				visited.add((pos - 1, new_time))
				queue.append((pos - 1, new_time))
		
		# Change direction at safety islands
		if pos in d and next_green_time >= 1 + time:
			new_time = 1 + time
			if (pos, new_time) not in visited:
				visited.add((pos, new_time))
				queue.append((pos, new_time))
	
	# If we exhaust the queue without reaching the end, it's impossible
	return -1


# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
d = list(map(int, data[2:2 + m]))
g = int(data[2 + m])
r = int(data[2 + m + 1])

# Output the result
print(min_time_to_cross(n, d, g, r))
