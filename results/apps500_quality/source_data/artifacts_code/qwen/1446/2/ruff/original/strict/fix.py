import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

c = list(map(int, data[3:3+k]))
edges = []
index = 3+k
for _ in range(m):
    u = int(data[index])-1
    v = int(data[index+1])-1
    x = int(data[index+2])
    edges.append((u, v, x))
    edges.append((v, u, x))
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
    dist = [float('inf')] * n
    dist[i] = 0
    pq = [(0, i)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for neighbor, edge_cost in adj[node]:
            new_cost = cost + edge_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return dist[j] if dist[j] != float('inf') else -1

# Check if the type-distribution is correct
correct = True
for i in range(k):
    for j in range(k):
        if i != j:
            if min_cost(sum(c[:i]), sum(c[:j])) == -1:
                correct = False
                break
    if not correct:
        break

if correct:
    print("Yes")
    for i in range(k):
        for j in range(k):
            if i == j:
                print(0, end=' ')
            else:
                print(min_cost(sum(c[:i]), sum(c[:j])), end=' ')
        print()
else:
    print("No")
