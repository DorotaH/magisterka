def can_escape(maze):
	n, m = len(maze), len(maze[0])
	start = (n - 1, m - 1)
	good_people = []
	bad_people = []

	# Collect the positions of good people and bad people
	for i in range(n):
		for j in range(m):
			if maze[i][j] == "G":
				good_people.append((i, j))
			elif maze[i][j] == "B":
				bad_people.append((i, j))

	# Function to check if a cell is within the maze boundaries
	def in_bounds(x, y):
		return 0 <= x < n and 0 <= y < m

	# Function to check if a cell is empty
	def is_empty(x, y):
		return maze[x][y] == "."

	# Function to check if a cell is blocked
	def is_blocked(x, y):
		return maze[x][y] == "#"

	# Function to perform BFS to check if a person can escape
	def can_escape_from(person):
		queue = [person]
		visited = set([person])
		while queue:
			x, y = queue.pop(0)
			if (x, y) == start:
				return True
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				nx, ny = dx + x, dy + y
				if in_bounds(nx, ny) and (nx, ny) not in visited:
					if is_empty(nx, ny):
						visited.add((nx, ny))
						queue.append((nx, ny))
					elif is_blocked(nx, ny):
						visited.add((nx, ny))
		return False

	# Check if all good people can escape and no bad people can escape
	for good in good_people:
		if not can_escape_from(good):
			return False
	for bad in bad_people:
		if can_escape_from(bad):
			return False

	return True


def solve():
	import sys

	input = sys.stdin.read
	data = input().split()

	index = 0
	t = int(data[index])
	index += 1
	results = []

	for _ in range(t):
		n = int(data[index])
		m = int(data[1 + index])
		index += 2
		maze = []
		for _ in range(n):
			maze.append(data[index])
			index += 1
		if can_escape(maze):
			results.append("Yes")
		else:
			results.append("No")

	for result in results:
		print(result)


# Call the solve function
solve()
