import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

# Parse the adjacency matrix
a = []
index = 3
for _ in range(n):
	row = list(map(int, data[index : m + index]))
	a.append(row)
	index += m

# Parse the log events
events = []
for _ in range(k):
	x = int(data[index]) - 1
	y = int(data[1 + index]) - 1
	events.append((x, y))
	index += 2

# Initialize the number of notifications for each employee
notifications = [0] * n

# Process each event
for x, y in events:
	# All other participants in chat y receive a notification
	for i in range(n):
		if a[i][y] == 1 and i != x:
			notifications[i] += 1

# Print the result
print(" ".join(map(str, notifications)))
