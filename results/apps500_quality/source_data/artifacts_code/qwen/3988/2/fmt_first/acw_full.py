import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
s = int(data[2])

edges = []
for i in range(3, 3 + 2 * m, 2):
	t = int(data[i])
	u = int(data[i + 1])
	v = int(data[i + 2])
	edges.append((t, u, v))


# Function to find the maximum number of reachable vertices
def max_reachable():
	from collections import deque

	visited = set()
	q = deque([s])
	visited.add(s)
	for t, u, v in edges:
		if t == 1 or u in visited:
			q.append(v)
		if t == 1 or v in visited:
			q.append(u)
	return len(visited)


# Function to find the minimum number of reachable vertices
def min_reachable():
	from collections import deque

	visited = set()
	q = deque([s])
	visited.add(s)
	for t, u, v in edges:
		if t == 1 or u not in visited:
			q.append(v)
		if t == 1 or v not in visited:
			q.append(u)
	return len(visited)


# Find the number of reachable vertices in the initial graph
max_reachable_count = max_reachable()
min_reachable_count = min_reachable()

# Find the directions for the maximum reachable vertices
max_directions = []
for t, u, v in edges:
	if t == 2:
		max_directions.append("+")
	else:
		max_directions.append("-")

# Find the directions for the minimum reachable vertices
min_directions = []
for t, u, v in edges:
	if t == 2:
		min_directions.append("-")
	else:
		min_directions.append("+")

# Output the results
print(max_reachable_count)
print("".join(max_directions))
print(min_reachable_count)
print("".join(min_directions))
