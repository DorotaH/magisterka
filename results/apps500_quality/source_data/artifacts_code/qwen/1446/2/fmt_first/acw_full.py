from collections import defaultdict
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

c = list(map(int, data[3 : k + 3]))
edges = []
index = k + 3
for _ in range(m):
	u = int(data[index]) - 1
	v = int(data[1 + index]) - 1
	x = int(data[2 + index])
	edges.extend(((u, v, x), (v, u, x)))
	index += 3

# Create adjacency list for the graph
adj = defaultdict(list)
for u, v, x in edges:
	adj[u].append((v, x))
	adj[v].append((u, x))


# Function to find the minimum cost to move energy from bacteria i to bacteria j
def min_cost(i, j):
	if i == j:
		return 0
	dist = [float("inf")] * n
	dist[i] = 0
	pq = [(0, i)]
	while pq:
		cost, node = heapq.heappop(pq)
		if cost > dist[node]:
			continue
		for neighbor, edge_cost in adj[node]:
			new_cost = edge_cost + cost
			if new_cost < dist[neighbor]:
				dist[neighbor] = new_cost
				heapq.heappush(pq, (new_cost, neighbor))
	return dist[j] if dist[j] != float("inf") else -1


# Check if the type-distribution is correct
correct = True
for i in range(k):
	for j in range(k):
		if i != j and min_cost(sum(c[:i]), sum(c[:j])) == -1:
			correct = False
			break
	if not correct:
		break

if correct:
	print("Yes")
	for i in range(k):
		for j in range(k):
			if i == j:
				print(0, end=" ")
			else:
				print(min_cost(sum(c[:i]), sum(c[:j])), end=" ")
		print()
else:
	print("No")
